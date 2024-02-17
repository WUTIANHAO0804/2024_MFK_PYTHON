def caesar_cipher(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message
message = input()
encrypted_message = caesar_cipher(message)
print(encrypted_message)