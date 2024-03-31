import numpy as np

# Считываем данные из файла
data = np.genfromtxt('input.csv', delimiter=',')

# Суммируем количество появлений каждого цвета
color_counts = np.sum(data, axis=0)

# Находим индекс цвета с максимальным количеством появлений
most_popular_color_index = np.argmax(color_counts)

# Выводим номер наиболее часто встречающегося цвета
print(most_popular_color_index + 1)