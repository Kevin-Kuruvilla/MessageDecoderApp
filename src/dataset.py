import random
import pandas as pd
from tqdm import tqdm
from caesarcipher import caesar_cipher
from vigenerecipher import vigenere_cipher

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
        if i % 2 == 0:
            random_key = random.randint(1,25)
            messages[i] = caesar_cipher(messages[i], random_key)
            labels[i] = 1
        elif i % 2 == 1:
            keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            random_key = ''.join([random.choice(keys) for _ in range(10)])
            messages[i] = vigenere_cipher(messages[i], random_key)

    return messages, labels