def caesar_decipher(text, key):
  text_chars = list(text)

  for i in range(len(text_chars)):
    char = text_chars[i]

    if char.isalpha():
      start = ord('A') if char.isupper() else ord('a')
      numChar = ord(char) - start
      numChar = (numChar - key) % 26
      text_chars[i] = chr(numChar + start)
    elif char.isnumeric():
      start = ord('0')
      numChar = ord(char) - start
      numChar = (numChar - key) % 10
      text_chars[i] = chr(numChar + start)

  return ''.join(text_chars)