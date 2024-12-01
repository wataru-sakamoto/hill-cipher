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