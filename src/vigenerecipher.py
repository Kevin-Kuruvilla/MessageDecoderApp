import re


def find_char(key_pair):
    char = ''
    msg_char = key_pair[0]
    key_char = key_pair[1]

    # Finding ASCII value for shifted character
    if msg_char.isupper():
        if key_char.isupper():
            char = (ord(msg_char) + ord(key_char) - 2 * ord('A'))
        elif key_char.islower():
            char = (ord(msg_char) + ord(key_char) - ord('A') - ord('a') + 26)
        elif key_char.isdigit():
            char = (ord(msg_char) + ord(key_char) - ord('A') - ord('0') + 52)
    elif msg_char.islower():
        if key_char.isupper():
            char = (ord(msg_char) + ord(key_char) - ord('a') + 26 - ord('A'))
        elif key_char.islower():
            char = (ord(msg_char) + ord(key_char) - 2 * ord('a') + 52)
        elif key_char.isdigit():
            char = (ord(msg_char) + ord(key_char) - ord('a') + 26 - ord('0') + 52)
    elif msg_char.isdigit():
        if key_char.isupper():
            char = (ord(msg_char) + ord(key_char) - ord('0') + 52 - ord('A'))
        elif key_char.islower():
            char = (ord(msg_char) + ord(key_char) - ord('0') + 52 - ord('a') + 26)
        elif key_char.isdigit():
            char = (ord(msg_char) + ord(key_char) - 2 * ord('0') + 104)

    # Returning character in appropriate range
    return char % 62


def build_vigenere_table():
    table = {}

    # Defining characters in table
    alphabets_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabets_lower = alphabets_upper.lower()
    digits = "0123456789"


    for msg_char in alphabets_upper + alphabets_lower + digits:
        for key_char in alphabets_upper + alphabets_lower + digits:
            pair = msg_char, key_char
            char = find_char(pair)

            if char in range(0, 26):
              table[pair] = chr(char + ord('A'))
            elif char in range (26, 52):
              table[pair] = chr(char - 26 + ord('a'))
            elif char in range(52, 62):
              table[pair] = chr(char - 52 + ord('0'))

    return table


def vigenere_cipher(text, key):
    # Building vigenere table
    vigenere_table = build_vigenere_table()

    result = ""
    key_length = len(key)

    # Regular expression for supported characters
    pattern = re.compile(r'[A-Za-z0-9]')

    for i, char in enumerate(text):
        # Repeating key necessary amount of times
        key_char = key[i % key_length]

        # Shifting alphanumeric characters
        if pattern.match(char):
            result += vigenere_table[(char, key_char)]
        # Preserving non-alphanumeric characters
        else:
            result += char

    return result