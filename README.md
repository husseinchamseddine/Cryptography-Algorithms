
# Ciphering and Deciphering Project

## Overview

This project provides ciphering and deciphering capabilities using the following algorithms:
- AES (Advanced Encryption Standard)
- Extended Euclidean Algorithm
- Hill Cipher
- Playfair Cipher

Additionally, the project includes a web page interface for easy use of these algorithms.

## Features

- **AES Encryption/Decryption**: Symmetric encryption technique using the AES algorithm.
- **Extended Euclidean Algorithm**: Used for finding the greatest common divisor and for solving linear Diophantine equations.
- **Hill Cipher**: A polygraphic substitution cipher based on linear algebra.
- **Playfair Cipher**: A digraph substitution cipher that encrypts pairs of letters.


## Usage

### Running the Web Application

1. Navigate to the project directory.
2. Start the Flask web server:

    ```sh
    python app.py
    ```

3. Open your web browser and go to `http://127.0.0.1:5000`.

### Using the Web Interface

- **AES**: Input your plaintext and key, then select either encryption or decryption.
- **Extended Euclidean Algorithm**: Input your two integers to find their greatest common divisor and coefficients.
- **Hill Cipher**: Input your plaintext, key matrix, and choose either encryption or decryption.
- **Playfair Cipher**: Input your plaintext and key, then select either encryption or decryption.

## Algorithms

### AES (Advanced Encryption Standard)

AES is a symmetric encryption algorithm widely used across the globe. It encrypts data in blocks of 128 bits using keys of 128, 192, or 256 bits.

### Extended Euclidean Algorithm

This algorithm extends the Euclidean algorithm to find integer coefficients for the linear combination of two integers that equals their greatest common divisor.

### Hill Cipher

The Hill cipher is a polygraphic substitution cipher that uses linear algebra. A block of plaintext letters is represented as a vector and multiplied by a key matrix to produce ciphertext.

### Playfair Cipher

The Playfair cipher encrypts pairs of letters (digraphs), making it more complex than simple substitution ciphers. It uses a 5x5 grid of letters constructed using a keyword.

