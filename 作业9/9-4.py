import pandas as pd

# Читаем CSV-файл
df = pd.read_csv('input.csv')

# Вычисляем сумму дивидендов для каждой ценной бумаги
total_dividends = df.sum()

# Проверяем, достаточно ли суммы дивидендов для покупки нового Мерседеса
if total_dividends.sum() >= 8000000:
    enough_for_mercedes = 1
else:
    enough_for_mercedes = 0

# Находим наиболее прибыльную ценную бумагу
most_profitable_stock = total_dividends.idxmax()

print(enough_for_mercedes, most_profitable_stock)
