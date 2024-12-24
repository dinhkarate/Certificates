# Ma trận Playfair (của bạn đã cung cấp)
playfair_matrix = [
    ['J', 'K', 'C', 'D', 'E'],
    ['U', 'N', 'P', 'Q', 'S'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['R', 'A', 'L', 'G', 'O'],
    ['B', 'I', 'T', 'H', 'M']
]

# Hàm tìm vị trí của ký tự trong ma trận
def find_position(char, matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == char:
                return row, col
    # Nếu không tìm thấy ký tự, in ra lỗi và trả về None, None
    print(f"Character '{char}' not found in the matrix!")
    return None, None

# Hàm chuẩn bị thông điệp (loại bỏ khoảng trắng, thay 'J' thành 'I', chia thành cặp)
def prepare_message(message):
    message = message.replace(" ", "").upper()  # Loại bỏ khoảng trắng và chuyển thành chữ hoa
    message = message.replace('J', 'I')  # Thay 'J' bằng 'I' nếu có
    
    # Bỏ qua các ký tự không phải chữ cái (chỉ giữ lại A-Z)
    message = ''.join([char for char in message if char.isalpha()])

    # Nếu thông điệp có số lượng ký tự lẻ, thêm 'X' vào cuối
    if len(message) % 2 != 0:
        message += 'X'

    pairs = []
    i = 0
    while i < len(message):
        pairs.append(message[i:i + 2])  # Thêm cặp chữ cái
        i += 2
    return pairs

# Hàm mã hóa cặp chữ cái
def encrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)
    
    # Kiểm tra nếu các ký tự không tìm thấy trong ma trận
    if row1 is None or row2 is None:
        return ""
    
    # Quy tắc 1: Cùng hàng
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    
    # Quy tắc 2: Cùng cột
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    
    # Quy tắc 3: Khác hàng và cột (hình chữ nhật)
    else:
        return matrix[row1][col2] + matrix[row2][col1]

# Hàm mã hóa thông điệp
def playfair_encrypt(message, matrix):
    pairs = prepare_message(message)
    encrypted_message = ''
    for pair in pairs:
        encrypted_message += encrypt_pair(pair, matrix)
    return encrypted_message

# Hàm giải mã cặp chữ cái (quy tắc ngược lại với mã hóa)
def decrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)
    
    # Kiểm tra nếu các ký tự không tìm thấy trong ma trận
    if row1 is None or row2 is None:
        return ""
    
    # Quy tắc 1: Cùng hàng
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    
    # Quy tắc 2: Cùng cột
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    
    # Quy tắc 3: Khác hàng và cột (hình chữ nhật)
    else:
        return matrix[row1][col2] + matrix[row2][col1]

# Hàm giải mã thông điệp
def playfair_decrypt(encrypted_message, matrix):
    pairs = [encrypted_message[i:i + 2] for i in range(0, len(encrypted_message), 2)]
    decrypted_message = ''
    for pair in pairs:
        decrypted_message += decrypt_pair(pair, matrix)
    return decrypted_message

# Ví dụ thông điệp
message = "I only regret that I have but one life to give for my country"

# Mã hóa thông điệp
encrypted_message = playfair_encrypt(message, playfair_matrix)
print("Encrypted Message:", encrypted_message)

# Giải mã thông điệp
decrypted_message = playfair_decrypt(encrypted_message, playfair_matrix)
print("Decrypted Message:", decrypted_message)
