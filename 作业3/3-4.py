with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
n = int(lines[0])
names = [line.strip() for line in lines[1:n+1]]
birthdates = [line.strip() for line in lines[n+1:]]
data = zip(names, birthdates)
with open('output.txt', 'w', encoding='utf-8') as file:
    for name, birthdate in data:
        print(name, birthdate, sep='\t', file=file)
