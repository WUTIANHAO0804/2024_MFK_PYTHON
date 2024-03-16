# Чтение данных из файла input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

animal_dict = {}

# Обработка данных и добавление информации о животных в словарь
for line in lines:
    animal_info = line.strip().split()
    if len(animal_info) >= 3:
        animal = animal_info[1]
        gender = animal_info[2]
        if animal in animal_dict:
            animal_dict[animal].add(gender)
        else:
            animal_dict[animal] = {gender}

# Поиск видов животных, которые могут давать потомство
reproductive_animals = [animal for animal, genders in animal_dict.items() if len(genders) > 1]

# Вывод результатов
if reproductive_animals:
    for animal in sorted(reproductive_animals, key=len):
        print(animal)
else:
    print(0)