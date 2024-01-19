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
    print(f"Modular inverse: {t % m}")
    return t % m
  

def rsacipher(text, key):  
  p = key[0]
  q = key[1]
  n = p * q
  k = (p - 1) * (q - 1)
  
  e = key[2]
  # modular_inverse(e, k)
  
  text_chars = list(text)

  for i in range(len(text_chars)):
    iterations = e
    char = text_chars[i]
    message = 1
    multiplier = ord(char)
    
    while(iterations > 0):
      message *= multiplier
      message %= n
      iterations -= 1

    text_chars[i] = str(message)
  
  return text_chars


def rsadecipher(ciphertext, key):
  d = key[0]
  n = key[1]
  deciphered_text = ""
  
  for num in ciphertext:
    iterations = d
    char = 1
    multiplier = int(num)
    
    while(iterations > 0):
      char *= multiplier
      char %= n
      iterations -= 1
    
    deciphered_text += chr(char)
  
  return ''.join(deciphered_text)