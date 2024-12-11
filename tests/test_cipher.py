import unittest
import numpy as np
from hillcipher.cipher import HillCipher

class TestHillCipher(unittest.TestCase):
    def setUp(self):
        """
        Set up a HillCipher instance for testing.
        """
        self.cipher = HillCipher(block_size=2)
        self.cipher.generate_key()

    def test_key_generation(self):
        """
        Test that the generated key is a valid invertible matrix.
        """
        key = self.cipher.key
        self.assertIsNotNone(key, "Key should not be None")
        self.assertEqual(key.shape, (2, 2), "Key should be a 2x2 matrix")
        self.assertTrue(HillCipher._is_invertible(key), "Key should be invertible")

    def test_encryption_and_decryption(self):
        """
        Test that encryption followed by decryption returns the original text.
        """
        plaintext = "HELLO"
        ciphertext = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(ciphertext)
        self.assertEqual(decrypted.strip('X'), plaintext, "Decrypted text should match the original plaintext")
