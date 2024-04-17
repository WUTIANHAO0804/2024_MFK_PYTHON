import pandas as pd

# Читаем CSV-файл
df = pd.read_csv('input.csv')

# Проверяем каждую строку на выполнение неравенства треугольника
df['is_triangle'] = (df['a'] < df['b'] + df['c']) & (df['b'] < df['a'] + df['c']) & (df['c'] < df['a'] + df['b'])

# Считаем количество строк, где 'is_triangle' равно True
num_triangles = df['is_triangle'].sum()

print(num_triangles)