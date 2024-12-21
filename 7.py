def xor_decrypt(ciphertext, key):
    decrypted_data = bytearray()
    key_length = len(key)

    for i, byte in enumerate(ciphertext):
        decrypted_byte = byte ^ key[i % key_length]
        decrypted_data.append(decrypted_byte)

    return bytes(decrypted_data)

# Đọc tấm ảnh đã được mã hóa từ file
with open("crypto01.jpg", "rb") as file:
    encrypted_data = file.read()

# Khóa XOR đã được sử dụng để mã hóa
encryption_key = b'uithcm'

# Giải mã tấm ảnh
decrypted_data = xor_decrypt(encrypted_data, encryption_key)

# Ghi tấm ảnh đã giải mã ra file
with open("decrypted_image.jpg", "wb") as file:
    file.write(decrypted_data)

print("Đã giải mã tấm ảnh.")