import os
import pickle
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Embedding, Conv1D, GlobalAveragePooling1D, Dense
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from dataset import create_dataset

# Parameters for message classifier
num_samples = 100_000
vocab_size = 10_000
max_length = 120
embedding_dim = 16
num_epochs = 4

class MessageClassifier:
    def __init__(self):
        self.num_samples = num_samples
        self.vocab_size = vocab_size
        self.max_length = max_length
        self.embedding_dim = embedding_dim
        self.num_epochs = num_epochs
        self.padding_type = 'post'
        self.trunc_type = 'post'
        self.oov_tok = "<OOV>"
        self.model, self.tokenizer = self.__get_model()

    def __get_model(self):
        model = None
        tokenizer = None

        # Disable info messages from tensorflow
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

        # check if model is already trained
        if os.path.exists("out/trained_model.h5") and os.path.exists("out/tokenizer.pickle"):
            print("\nLoading existing model.")

            model = load_model("out/trained_model.h5")
            with open("out/tokenizer.pickle", 'rb') as handle:
                tokenizer = pickle.load(handle)

            print("Model and tokenizer loaded.\n")
        else:
            print("\nModel not found, creating new one...")
            model, tokenizer = self.__build_model()

            print("\nModel created, saving...")
            model.save("out/trained_model.h5")
            with open("out/tokenizer.pickle", 'wb') as handle:
                pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

            print("Model trained and saved.\n")

        return model, tokenizer
    
    def __preprocess_data(self, tokenizer, raw_text, raw_labels):
        # convert words to sequences and add padding
        sequences = tokenizer.texts_to_sequences(raw_text)
        padded_sequences = pad_sequences(sequences, maxlen=self.max_length, 
                                        padding=self.padding_type, truncating=self.trunc_type)

        # convert lists into numpy arrays to make it work with TensorFlow 2.
        return np.array(padded_sequences), np.array(raw_labels)

    def __build_model(self):
        # get training and testing data
        training_sentences, testing_sentences, training_labels, testing_labels = create_dataset(self.num_samples)

        # set up tokenizer
        tokenizer = Tokenizer(num_words=self.vocab_size, oov_token=self.oov_tok)
        tokenizer.fit_on_texts(training_sentences)
        
        # preprocess data
        training_padded, training_labels = self.__preprocess_data(tokenizer, training_sentences, training_labels)
        testing_padded, testing_labels = self.__preprocess_data(tokenizer, testing_sentences, testing_labels)

        # define model
        print("\nCreating model...")
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
        print("\nTraining model...")
        model.fit(training_padded,
                  training_labels,
                  epochs=self.num_epochs,
                  validation_data=(testing_padded, testing_labels))

        return model, tokenizer

    def predict_message(self, message):
        sequences = self.tokenizer.texts_to_sequences([message])
        padded_sequences = pad_sequences(sequences, maxlen=self.max_length, padding=self.padding_type, truncating=self.trunc_type)
        return self.model.predict(padded_sequences, verbose=0)[0][0]