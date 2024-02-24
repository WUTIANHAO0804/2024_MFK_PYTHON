with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for line in filter(lambda x: 'ё' in x.lower(), map(str.strip, lines)):
    print(line)