from MessageClassifier import MessageClassifier
from caesarcipher import caesar_cipher
from vigenerecipher import vigenere_cipher
from rsacipher import rsacipher
from affinecipher import affine_cipher

# Instantiate Message Classifier
classifier = MessageClassifier()

# Create example messages
message = "The X-47B, an unmanned combat air vehicle, has a wingspan of 62 feet and can reach speeds up to Mach 0.9, utilizing its advanced AI algorithms for autonomous operations."
caesar_message = caesar_cipher(message, 5)
vigenere_message = vigenere_cipher(message, "KEY")
rsa_message = ''.join(rsacipher(message, (457, 863, 11)))
affine_message = affine_cipher(message, (11, 20))

# Create demo
def demo(message):
    prediction = classifier.predict_message(message)
    print(f"The message \"{message}\" is encrypted with the {prediction} cipher.\n")

demo(message)
demo(caesar_message)
demo(vigenere_message)
demo(rsa_message)
demo(affine_message)
