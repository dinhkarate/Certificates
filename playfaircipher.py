# Playfair Cipher Implementation in Python

def remove_duplicates(key):
    """ Remove duplicate characters from the key, keeping the order. """
    seen = set()
    return ''.join([char for char in key if not (char in seen or seen.add(char))])

def create_playfair_matrix(key):
    """ Create a 5x5 Playfair matrix using the key. """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is omitted
    key = remove_duplicates(key.upper())  # Remove duplicates and uppercase
    matrix = key + ''.join([char for char in alphabet if char not in key])
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def display_matrix(matrix):
    """ Display the Playfair matrix in 5x5 format. """
    for row in matrix:
        print(' '.join(row))
    
def prepare_text(text):
    """ Prepare the text by removing spaces and handling I/J substitution. """
    text = text.replace('J', 'I').replace(' ', '').upper()
    # If the text has an odd number of characters, add an 'X' at the end
    if len(text) % 2 != 0:
        text += 'X'
    return text

def find_position(matrix, char):
    """ Find the row and column of a character in the matrix. """
    for i, row in enumerate(matrix):
        if char in row:
            return (i, row.index(char))
    return None

def encrypt_digraph(matrix, digraph):
    """ Encrypt a pair of characters (digraph) using the Playfair cipher rules. """
    row1, col1 = find_position(matrix, digraph[0])
    row2, col2 = find_position(matrix, digraph[1])
    
    # If they are in the same row
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    # If they are in the same column
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    # If they form a rectangle
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_digraph(matrix, digraph):
    """ Decrypt a pair of characters (digraph) using the Playfair cipher rules. """
    row1, col1 = find_position(matrix, digraph[0])
    row2, col2 = find_position(matrix, digraph[1])
    
    # If they are in the same row
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    # If they are in the same column
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    # If they form a rectangle
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_encrypt(matrix, plaintext):
    """ Encrypt the plaintext using the Playfair cipher. """
    plaintext = prepare_text(plaintext)
    digraphs = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]
    cipher_text = ''.join([encrypt_digraph(matrix, digraph) for digraph in digraphs])
    return cipher_text

def playfair_decrypt(matrix, ciphertext):
    """ Decrypt the ciphertext using the Playfair cipher. """
    digraphs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    decrypted_text = ''.join([decrypt_digraph(matrix, digraph) for digraph in digraphs])
    return decrypted_text

def main():
    # Input Key and Text
    key = input("Enter the key: ")
    mode = input("Choose mode (encrypt/decrypt): ").lower()
    text = input("Enter the message: ")
    
    # Create Playfair matrix
    matrix = create_playfair_matrix(key)
    print("\nPlayfair Matrix:")
    display_matrix(matrix)
    
    if mode == 'encrypt':
        encrypted_text = playfair_encrypt(matrix, text)
        print("\nEncrypted Text: ", encrypted_text)
    elif mode == 'decrypt':
        decrypted_text = playfair_decrypt(matrix, text)
        print("\nDecrypted Text: ", decrypted_text)
    else:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
