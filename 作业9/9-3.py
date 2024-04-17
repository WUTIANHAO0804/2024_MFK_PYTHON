import pandas as pd

# Читаем CSV-файл
df = pd.read_csv('input.csv')

# Вычисляем средний выигрыш для каждого автомата
average_wins = df.mean()

# Находим автомат с максимальным средним выигрышем
max_wins_machine = average_wins.idxmax()

print(max_wins_machine)