import numpy as np

class HillCipher:
    def __init__(self, block_size=2):
        """
        Initialize the Hill Cipher class.
        :param block_size: Size of encryption blocks (default: 2)
        """
        self.block_size = block_size
        self.key = None

    def generate_key(self):
        """
        Generate an invertible matrix and set it as the key for this instance.
        """
        self.key = self._generate_invertible_matrix(self.block_size)
        print("Generated encryption key (matrix):\n", self.key)
        
    def set_key(self, key):
        """
        Manually set the key for this instance.
        :param key: Encryption key (matrix)
        """
        self.key = np.array(key)
        if not self._is_invertible(self.key):
            raise ValueError("The provided key is not an invertible matrix.")

    def encrypt(self, plaintext):
        """
        Encrypt plaintext using the instance's key.
        :param plaintext: Text to be encrypted
        :return: Ciphertext
        """
        if self.key is None:
            raise ValueError("Encryption key is not set.")
        return self._process_text(plaintext, self.key)

    def decrypt(self, ciphertext):
        """
        Decrypt ciphertext using the instance's key.
        :param ciphertext: Text to be decrypted
        :return: Decrypted plaintext
        """
        if self.key is None:
            raise ValueError("Encryption key is not set.")
        inv_key = self._mod_inverse_matrix(self.key)
        return self._process_text(ciphertext, inv_key)

    @classmethod
    def generate_key(cls, block_size):
        """
        Class method: Generate an invertible matrix of the specified block size.
        :param block_size: Size of the matrix
        :return: Invertible matrix
        """
        return cls._generate_invertible_matrix(block_size)

    @classmethod
    def encrypt(cls, plaintext, key):
        """
        Class method: Encrypt plaintext using the provided key.
        :param plaintext: Text to be encrypted
        :param key: Encryption key (matrix)
        :return: Ciphertext
        """
        return cls._process_text(plaintext, key)

    @classmethod
    def decrypt(cls, ciphertext, key):
        """
        Class method: Decrypt ciphertext using the provided key.
        :param ciphertext: Text to be decrypted
        :param key: Encryption key (matrix)
        :return: Decrypted plaintext
        """
        inv_key = cls._mod_inverse_matrix(key)
        return cls._process_text(ciphertext, inv_key)

    @staticmethod
    def _generate_invertible_matrix(size):
        """
        Generate an invertible matrix of the specified size.
        :param size: Size of the matrix
        :return: Invertible matrix
        """
        while True:
            matrix = np.random.randint(1, 10, (size, size))
            if HillCipher._is_invertible(matrix):
                return matrix

    @staticmethod
    def _is_invertible(matrix, mod=26):
        """
        Check if a matrix is invertible modulo 26.
        :param matrix: Matrix to check
        :param mod: Modulus value (default: 26)
        :return: True if invertible, False otherwise
        """
        det = int(np.round(np.linalg.det(matrix)))
        return np.gcd(det, mod) == 1

    @staticmethod
    def _mod_inverse_matrix(matrix, mod=26):
        """
        Compute the modular inverse of a matrix.
        :param matrix: Original matrix
        :param mod: Modulus value
        :return: Modular inverse of the matrix
        """
        det = int(np.round(np.linalg.det(matrix)))  # Determinant of the matrix
        det_inv = pow(det, -1, mod)  # Modular inverse of the determinant
        adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod  # Adjugate matrix
        return (det_inv * adjugate) % mod

    @staticmethod
    def _process_text(text, matrix):
        """
        Process plaintext or ciphertext in blocks.
        :param text: Text to process
        :param matrix: Matrix to use for processing
        :return: Processed text
        """
        block_size = matrix.shape[0]
        text = text.upper().replace(" ", "")  # Convert to uppercase and remove spaces
        padding_length = (-len(text)) % block_size
        text += 'X' * padding_length  # Add padding if needed
        blocks = [text[i:i + block_size] for i in range(0, len(text), block_size)]
        result_blocks = []
        for block in blocks:
            vector = np.array([ord(char) - 65 for char in block])  # Convert characters to numbers (A=0, B=1, ...)
            result_vector = np.dot(matrix, vector) % 26
            result_blocks.append(''.join(chr(c + 65) for c in result_vector))
        return ''.join(result_blocks)

# Example usage
if __name__ == "__main__":
    # Using class methods
    block_size = 2
    key = HillCipher.generate_key(block_size)  # Generate key using class method
    print("Generated key (class method):\n", key)

    plaintext = "HELLO"
    ciphertext = HillCipher.encrypt(plaintext, key)  # Encrypt using class method
    print("Ciphertext (class method):", ciphertext)

    decrypted = HillCipher.decrypt(ciphertext, key)  # Decrypt using class method
    print("Decrypted text (class method):", decrypted)

    # Using instance methods
    cipher = HillCipher(block_size=2)
    cipher.generate_key()  # Generate key using instance method
    ciphertext_instance = cipher.encrypt(plaintext)  # Encrypt using instance method
    print("Ciphertext (instance method):", ciphertext_instance)
    decrypted_instance = cipher.decrypt(ciphertext_instance)  # Decrypt using instance method
    print("Decrypted text (instance method):", decrypted_instance)