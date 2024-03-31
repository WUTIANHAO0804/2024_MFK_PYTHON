import numpy as np

# Считываем данные из файла
data = np.genfromtxt('input.csv', delimiter=',')

# Вычисляем стандартное отклонение для каждого клиента
std_dev = np.std(data, axis=1)

# Подсчитываем количество клиентов каждого типа
type_1_count = np.sum(std_dev <= 4)
type_2_count = np.sum(std_dev > 4)

# Определяем, кого в клубе больше
if type_1_count > type_2_count:
    result = 1
else:
    result = 2

# Выводим результат
print(result)
