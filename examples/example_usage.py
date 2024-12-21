from hillcipher import HillCipher

# Create a HillCipher instance
cipher = HillCipher(block_size=2)

# Generate a key
cipher.generate_key()
print("Generated Key:")
print(cipher.key)

# Encrypt a plaintext message
plaintext = "HELLO"
ciphertext = cipher.encrypt(plaintext)
print("\nPlaintext:", plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_text = cipher.decrypt(ciphertext)
print("\nDecrypted Text:", decrypted_text)

# Visualize the encryption process
print("\nEncryption Process Explanation:")
cipher.explain_encryption(plaintext)

# Visualize the decryption process
print("\nDecryption Process Explanation:")
cipher.explain_decryption(ciphertext)
