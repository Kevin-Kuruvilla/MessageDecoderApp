# MessageDecoderApp

## Overview
MessageDecoderApp is a tool for quickly encrypting and decrypting messages. It employs NLP and cryptography techniques to detect patterns in encrypted text and accurately decrypts them.

## Features
- **Encryption & Decryption**: Utilize the Caesar Cipher and Vigenere Cipher for secure message handling.
- **Classify ciphers**: The MessageClassifier module can distinguish between Caesar and Vigenere Ciphers with 97% accuracy.
- **User-Friendly Interface**: The classifier autonomously recognizes and solves messages, eliminating manual cipher identification.

## Requirements
- Python 3.10.8 (Note: Not compatible with Python 3.11)
- Kaggle API credentials
- Additional libraries as per `requirements.txt`

## Installation

1. Clone the repository to your local machine.
2. Install dependencies using `pip install -r requirements.txt` (recommended within a virtual environment).
3. Add your `kaggle.json` API credentials in the `data` directory.
4. Run the `setup.h` script to download the data.csv file (227 MB).

## Usage
- Execute `__init__.py` to start the application.

## Acknowledgements
- This project was in collaboration with [Jason Jee](https://github.com/jjeeeeee) who made the encryption and decryption algorithms in this project.