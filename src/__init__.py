from MessageClassifier import MessageClassifier
from caesarcipher import caesar_cipher
from vigenerecipher import vigenere_cipher

# Instantiate Message Classifier
classifier = MessageClassifier()

# Create example messages
message = "This message is caesar message"
caesar_message = caesar_cipher(message, 5)
vigenere_message = vigenere_cipher(message, "KEY")

# Create demo
def demo(message):
    print(f"{message} is encrypted with the ", end='')
    if classifier.predict_message(message) > 0.5:
        print("caesar cipher")
    else:
        print("vigenere cipher")

demo(caesar_message)
demo(vigenere_message)
print()