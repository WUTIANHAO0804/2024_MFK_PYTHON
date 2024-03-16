# Чтение данных из файла input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

animals = set()

# Обработка данных и добавление видов животных во множество
for line in lines:
    animal_info = line.strip().split()
    if len(animal_info) >= 2:
        animal = animal_info[1]
        animals.add(animal)

# Вывод видов животных в порядке увеличения длины названия
for animal in sorted(animals, key=len):
    print(animal)