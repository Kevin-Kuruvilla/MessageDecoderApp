import re

def affine_cipher(text, key):
    a = key[0]
    b = key[1]
    ALPHABET_LENGTH = 26
    cleaned_text = re.sub(r'[^A-Za-z0-9 ]', '', text) # remove special characters
    text_chars = list(cleaned_text)

    for i in range(len(text_chars)):
        char = text_chars[i]

        if(char.isalpha()):
            num_char = ord(char) - ord('A')

            #Encrypting char using formula a*x + b
            ciphered_char = ((a * num_char) + b) % ALPHABET_LENGTH
            text_chars[i] = chr(ciphered_char + ord('A'))
    
    return ''.join(text_chars)