import pandas as pd

# Читаем CSV-файл
df = pd.read_csv('input.csv', header=None)

# Вычисляем среднее значение попаданий для каждой области
average_hits = df.mean()

# Находим область с минимальным средним значением попаданий
min_hits_area = average_hits.idxmin() + 1  # idxmin возвращает индекс минимального значения, добавляем 1, так как области нумеруются с 1

print(min_hits_area)