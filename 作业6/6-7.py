from collections import defaultdict

# Чтение данных из файла input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

animal_count = defaultdict(int)

# Обработка данных и подсчет количества животных для каждого вида
for line in lines:
    animal_info = line.strip().split()
    if len(animal_info) >= 2:
        animal = animal_info[1]
        animal_count[animal] += 1

# Вывод результатов в порядке убывания количества
sorted_animal_count = sorted(animal_count.items(), key=lambda x: x[1], reverse=True)
for animal, count in sorted_animal_count:
    print(f"{animal} - {count}")