from MessageClassifier import MessageClassifier
from caesarcipher import caesar_cipher
from vigenerecipher import vigenere_cipher

# Parameters for message classifier
num_samples = 100_000
vocab_size = 10_000
max_length = 120
embedding_dim = 16
num_epochs = 4

# Instantiate Message Classifier
classifier = MessageClassifier(num_samples, vocab_size, max_length, embedding_dim, num_epochs)

# Create example messages
message = "This message is caesar message"
caesar_message = caesar_cipher(message, 5)
vigenere_message = vigenere_cipher(message, "KEY")

# Test example messages
if classifier.predict_message(caesar_message) > 0.5:
    print("caesar text")
else:
    print("vigenere text")

if classifier.predict_message(vigenere_message) > 0.5:
    print("caesar text")
else:
    print("vigenere text")
