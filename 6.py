# List of ASCII codes
ascii_codes = [
    87, 101, 108, 99, 111, 109, 101, 32, 116, 111, 32, 67, 114, 121, 112, 116, 
    111, 32, 73, 115, 108, 97, 110, 100, 33, 33, 33, 32
]

# Convert ASCII codes to characters and concatenate them
decoded_message = ''.join(chr(code) for code in ascii_codes)

# Output the decoded message
print(decoded_message)
