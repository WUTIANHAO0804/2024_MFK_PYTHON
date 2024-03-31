import numpy as np

# Считываем данные из файла
data = np.genfromtxt('input.csv', delimiter=',')

# Модифицируем массив в соответствии с условием задачи
modified_data = data.copy()
modified_data[1::2, ::2] /= 2
modified_data[::2, 1::2] /= 2

# Сохраняем модифицированный массив в файл
np.savetxt('output.csv', modified_data, delimiter=',', fmt='%g')
