with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
output_lines = []
for line in lines:
    words = line.split()
    processed_line = ' '.join(words[::2])  
    output_lines.append(processed_line)
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(output_lines))