import numpy as np

# Считываем данные из файла
data = np.genfromtxt('input.csv', delimiter=',')

# Вычисляем среднее значение побед по каждому дню
daily_avg_wins = np.mean(data, axis=0)

# Умножаем среднее значение побед на 1.5 и округляем вниз до целого
modified_value = np.floor(daily_avg_wins * 1.5).astype(int)

# Заменяем значение в первой строке на модифицированное значение
data[0] = modified_value

# Сохраняем модифицированный массив в файл
np.savetxt('output.csv', data, delimiter=',', fmt='%d')