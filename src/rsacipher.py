import math


def gcd(a, b):
  if(b == 0):
    return a
  else:
    return gcd(b, (a % b))


def extended_gcd(a, b):
  if(a == 0):
    return (b, 0, 1)
  else:
    extended_gcd_triple = extended_gcd(b % a, a)
    gcd = extended_gcd_triple[0]
    t = extended_gcd_triple[1]
    s = extended_gcd_triple[2]
    
    return (gcd, (s - (b // a) * t), t)
  

def modular_inverse(a, m):
  extended_gcd_triple = extended_gcd(a, m)
  gcd = extended_gcd_triple[0]
  t = extended_gcd_triple[1]
  
  if(gcd != 1):
    print("Module inverse does not exist")
    return None
  else:
    return t % m
  

def rsacipher(text, key):  
  text = text.upper()
  
  p = key[0]
  q = key[1]
  n = p * q
  k = (p - 1) * (q - 1)
  
  e = key[2]
  mod_inverse = modular_inverse(e, k)
  print(f"Modular inverse: {mod_inverse}")
  
  text_chars = list(text)

  for i in range(len(text_chars)):
    char = text_chars[i]

    if(char.isalpha()):
      num_char = ord(char) - ord('A') + 1
    elif(ord(char) == 32):
      num_char = 0
    
    text_chars[i] = str(num_char) if num_char >= 10 else "0" + str(num_char)
    
  text_as_nums = int(''.join(text_chars))
  print(text_as_nums)
  
  m = text_as_nums ** e
  ciphertext = m % n
  
  return ciphertext


def rsadecipher(ciphertext, key):
  d = key[0]
  n = key[1]
  
  m = str((ciphertext ** d) % n)
  
  if(len(m) % 2 == 1):
    m = "0" + m
  
  split_nums = [m[i:i+2] for i in range(0, len(m), 2)]
  deciphered_message = split_nums
  
  for i, num in enumerate(split_nums):
    if(int(num) == 0):
      deciphered_message[i] = " "
    else:
      deciphered_message[i] = chr(int(num) + ord('A') - 1)
  
  return ''.join(deciphered_message)