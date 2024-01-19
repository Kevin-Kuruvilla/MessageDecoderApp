import random
import pandas as pd
from tqdm import tqdm
from caesarcipher import caesar_cipher
from vigenerecipher import vigenere_cipher
from rsacipher import rsacipher
from affinecipher import affine_cipher
from math import gcd

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def create_dataset(num_samples):
    # define the columns in the dataset
    DATASET_COLUMNS = ["target", "ids", "date", "flag", "user", "text"]

    # load num_samples data from the dataset 
    dataset = pd.read_csv("data/data.csv", nrows=num_samples, names=DATASET_COLUMNS)

    # retrieve the text from the dataset
    messages = dataset['text'].copy()

    # by default, each message is labeled 0
    labels = [0] * len(messages)

    # using random keys apply caesar cipher and vigenere cipher in alternating pattern
    print("Creating dataset...")
    for i in tqdm(range(len(messages))):
        labels[i] = i % 5 # add label (0 = normal, 1 = caesar, 2 = vigenere, 3 = rsa, 4 = affine)
        if i % 5 == 1:
            random_key = random.randint(1,25)
            messages[i] = caesar_cipher(messages[i], random_key)
        elif i % 5 == 2:
            keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            random_key = ''.join([random.choice(keys) for _ in range(10)])
            messages[i] = vigenere_cipher(messages[i], random_key)
        elif i % 5 == 3:
            primes = [i for i in range(101, 1000) if is_prime(i)]
            p = random.choice(primes)
            q = random.choice(primes)
            while q == p:
                q = random.choice(primes)
            random_key = (p, q, 11)
            messages[i] = ''.join(rsacipher(messages[i], random_key))
        elif i % 5 == 4:
            a = random.choice([i for i in range(1, 26) if gcd(i, 26) == 1])
            b = random.randint(0, 25)
            random_key = (a,b)
            messages[i] = affine_cipher(messages[i], random_key)

    # 80% of data for training, rest for testing
    training_size = int(len(messages) * 0.8)

    # sentences
    training_sentences = messages[0:training_size]
    testing_sentences = messages[training_size:]

    # labels
    training_labels = labels[0:training_size]
    testing_labels = labels[training_size:]

    return training_sentences, testing_sentences, training_labels, testing_labels