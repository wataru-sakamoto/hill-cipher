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
