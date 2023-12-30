import os
import pickle
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Embedding, Conv1D, GlobalAveragePooling1D, Dense
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from dataset import create_dataset

class MessageClassifier:
    def __init__(self, num_samples, vocab_size, oov_tok, max_length, padding_type, trunc_type, embedding_dim, num_epochs):
        self.vocab_size = vocab_size
        self.oov_tok = oov_tok
        self.max_length = max_length
        self.padding_type = padding_type
        self.trunc_type = trunc_type
        self.embedding_dim = embedding_dim
        self.num_epochs = num_epochs
        self.num_samples = num_samples

        # check if model is already trained
        if os.path.exists("out/trained_model.h5") and os.path.exists("out/tokenizer.pickle"):
            print("Loading existing model.")

            self.model = load_model("out/trained_model.h5")
            with open("out/tokenizer.pickle", 'rb') as handle:
                self.tokenizer = pickle.load(handle)

            print("Model and tokenizer loaded.")
        else:
            print("Model not found, creating new one...")
            self.__build_model()

    def __build_model(self):
        # dataset
        messages, labels = create_dataset(self.num_samples)

        # 80% of data for training, rest for testing
        training_size = int(len(messages) * 0.8)

        # sentences
        training_sentences = messages[0:training_size]
        testing_sentences = messages[training_size:]

        # labels
        training_labels = labels[0:training_size]
        testing_labels = labels[training_size:]

        # set up tokenizer
        self.tokenizer = Tokenizer(num_words=self.vocab_size, oov_token=self.oov_tok)
        self.tokenizer.fit_on_texts(training_sentences)

        # preprocess training data
        training_sequences = self.tokenizer.texts_to_sequences(training_sentences)
        training_padded = pad_sequences(training_sequences, maxlen=self.max_length, 
                                        padding=self.padding_type, truncating=self.trunc_type)

        # preprocess testing data
        testing_sequences = self.tokenizer.texts_to_sequences(testing_sentences)
        testing_padded = pad_sequences(testing_sequences, maxlen=self.max_length, 
                                    padding=self.padding_type, truncating=self.trunc_type)

        # convert lists into numpy arrays to make it work with TensorFlow 2.x
        training_padded = np.array(training_padded)
        training_labels = np.array(training_labels)
        testing_padded = np.array(testing_padded)
        testing_labels = np.array(testing_labels)

        # define model
        print("Creating model...")
        model = Sequential([
            Embedding(self.vocab_size, self.embedding_dim, input_length=self.max_length),
            Conv1D(64, 5, activation='relu'),
            GlobalAveragePooling1D(),
            Dense(32, activation='relu'),
            Dense(1, activation='sigmoid')
        ])

        # compile model
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.summary()

        # train model
        print("Training model...")
        model.fit(training_padded,
                  training_labels,
                  epochs=self.num_epochs,
                  validation_data=(testing_padded, testing_labels))

        # save model
        print("Saving model...")

        self.model = model
        self.model.save("out/trained_model.h5")
        with open("out/tokenizer.pickle", 'wb') as handle:
            pickle.dump(self.tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

        print("Model trained and saved.")

    def predict_message(self, message):
        sequences = self.tokenizer.texts_to_sequences([message])
        padded_sequences = pad_sequences(sequences, maxlen=self.max_length, padding=self.padding_type, truncating=self.trunc_type)
        return self.model.predict(padded_sequences, verbose=0)[0][0]