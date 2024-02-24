with open('input.txt', 'r') as f:
    s = f.readline().strip()
reversed_s = ' '.join(word[::-1] for word in s.split())
print(reversed_s)