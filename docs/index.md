# Hill Cipher Documentation

Welcome to the documentation for the **Hill Cipher Library**. This library provides a Python implementation of the classical Hill Cipher encryption algorithm. It is designed for both practical use and educational purposes.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage Examples](#usage-examples)
4. [API Reference](#api-reference)
5. [Testing](#testing)
6. [Educational Features](#educational-features)
7. [Contributing](#contributing)
8. [License](#license)

---

## Introduction
The Hill Cipher is a classical encryption algorithm that leverages linear algebra concepts. This library allows users to:
- Encrypt and decrypt messages using the Hill Cipher.
- Learn the basics of cryptography and matrix operations.
- Explore the educational aspects of the algorithm with step-by-step explanations.

---

## Installation
To install the library, follow these steps:

### Clone the Repository
1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd hill-cipher
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Install via PyPI
If available, you can install the library from PyPI:
```bash
pip install hill-cipher
```
---

## Usage Examples
Here are some examples of how to use the Hill Cipher library.

### Encrypt and Decrypt a Message
```python
from hillcipher import HillCipher
```

### Create a HillCipher instance
```python
cipher = HillCipher(block_size=2)
cipher.generate_key()
```

### Encrypt a plaintext
```python
plaintext = "HELLO"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)
```

### Decrypt the ciphertext
```python
decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted text:", decrypted_text)
```

### Visualize the Encryption Process
```python
cipher.explain_encryption("HELLO")
```

### Visualize the Decryption Process
```python
cipher.explain_decryption("CIPHERTEXT")
```

---

## API Reference

### HillCipher Class
The HillCipher class provides the following methods:

- **`__init__(block_size=2)`**:
  Initializes the Hill Cipher with a specified block size.
  
- **`generate_key()`**:
  Generates a random invertible matrix as the encryption key.

- **`set_key(key)`**:
  Manually sets a matrix as the encryption key. Raises an error if the matrix is not invertible.

- **`encrypt(plaintext)`**:
  Encrypts a plaintext message using the current key.

- **`decrypt(ciphertext)`**:
  Decrypts a ciphertext message using the current key.

- **`explain_encryption(plaintext)`**:
  Provides a detailed explanation of the encryption process.

- **`explain_decryption(ciphertext)`**:
  Provides a detailed explanation of the decryption process.

---

## Testing

To ensure the library works correctly, run the provided test suite.

```bash
python -m unittest discover tests
```

---

## Educational Features

The Hill Cipher library includes features specifically designed for learning:

1. **Step-by-step Explanations**:
   - Use `explain_encryption` and `explain_decryption` methods to understand the inner workings of the algorithm.

2. **Custom Key Input**:
   - Set your own encryption key matrix using the `set_key` method to explore how matrix properties affect encryption.

---

## Contributing

We welcome contributions! Follow these steps to contribute:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```

3. Make your changes and commit them with a descriptive message:
    ```bash
    git commit -m "Add feature description"
    ```

4. Push your changes:
    ```bash
    git push origin feature-name
    ```

5. Submit a pull request on GitHub with a detailed explanation of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for more details.
