# Vigenère cipher encryption
def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    plaintext = plaintext.upper()

    key_index = 0
    for char in plaintext:
        if char.isalpha():
            # Encrypt only alphabetic characters
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
            key_index += 1  # Move to the next character in the key
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext += char
    
    return ciphertext

# Vigenère cipher decryption
def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    ciphertext = ciphertext.upper()

    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            # Decrypt only alphabetic characters
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted_char
            key_index += 1  # Move to the next character in the key
        else:
            # Non-alphabetic characters remain unchanged
            plaintext += char
    
    return plaintext

# Testing the Vigenère cipher with a message and a key
def test_vigenere_cipher():
    message = """I only regret that I have but one life to give for my country. 
                I have only one life, which I will devote to the service of my country. 
                I will give my life for my country's freedom and I shall die for its liberty."""
    key = "KEYEXAMPLE"  # A sample key, you can modify the key for testing
    
    print("Original Message:")
    print(message)
    
    # Encrypt the message
    encrypted_message = vigenere_encrypt(message, key)
    print("\nEncrypted Message:")
    print(encrypted_message)
    
    # Decrypt the message
    decrypted_message = vigenere_decrypt(encrypted_message, key)
    print("\nDecrypted Message:")
    print(decrypted_message)

# Run the test
test_vigenere_cipher()
