from collections import Counter

# Ввод длинного числа
number = input()

# Проведение частотного анализа
counter = Counter(number)

# Нахождение наиболее часто встречающейся цифры
most_common_digit = max(counter, key=counter.get)

print(f"{most_common_digit}")