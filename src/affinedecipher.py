def affine_decipher(text, key):
    a = key[0]
    b = key[1]
    a_inverse = 0
    ALPHABET_LENGTH = 26
    text_chars = list(text)

    # Finding modular inverse of a (mod 26)
    for i in range(26):
        if((a * i) % 26 == 1):
            a_inverse = i
            break

    for i in range(len(text_chars)):
        char = text_chars[i]

        if(char.isalpha()):
            num_char = ord(char) - ord('A')

            # Decrypting char using formula a^(-1)*(x - b) 
            ciphered_char = (a_inverse * (num_char - b)) % ALPHABET_LENGTH
            text_chars[i] = chr(ciphered_char + ord('A'))
    
    return ''.join(text_chars)