def decrypt_text(text):
    lines = text.split('\n')
    sorted_lines = sorted(lines, key=lambda x: len(x.split()))
    decrypted_lines = []
    for line in sorted_lines:
        words = line.split()
        sorted_words = sorted(words, key=lambda x: len(x))
        decrypted_line = ' '.join(sorted_words)
        decrypted_lines.append(decrypted_line)
    return '\n'.join(decrypted_lines)

# Чтение зашифрованного текста из файла
with open('poe_unpublished.txt', 'r') as file:
    encrypted_text = file.read()

# Расшифровка текста
decrypted_text = decrypt_text(encrypted_text)

# Запись расшифрованного текста в файл
with open('poe_decode_attempt.txt', 'w') as file:
    file.write(decrypted_text)