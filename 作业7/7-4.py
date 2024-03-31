import numpy as np

# Чтение входных данных из файла input.txt
with open('input.txt', 'r') as f:
    data = f.readlines()

start_profit = int(data[0].strip())
end_profit = int(data[1].strip())
days = int(data[2].strip())

# Создание массива фактической прибыли с поправкой на продуктивность
expected_profits = np.linspace(start_profit, end_profit, days)
actual_profits = []

for i in range(days):
    day_of_week = (i % 7) + 1
    
    if day_of_week == 1: # Понедельник
        actual_profit = expected_profits[i] / 3
    elif day_of_week == 5: # Пятница
        actual_profit = expected_profits[i] * 2
    else:
        actual_profit = expected_profits[i]
    
    actual_profits.append(actual_profit)

# Запись результатов в файл output.txt
with open('output.txt', 'w') as f:
    for profit in actual_profits:
        f.write(f'{profit:.2f}\n')