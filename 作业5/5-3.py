with open('med_research.txt', 'r') as file:
    data = [line.strip().split() for line in file]

# Транспонирование матрицы
transposed_data = []
for i in range(len(data[0])):
    transposed_row = [data[j][i] for j in range(len(data))]
    transposed_data.append(transposed_row)

# Запись данных в файл
with open('output.txt', 'w') as file:
    for row in transposed_data:
        file.write(' '.join(row) + '\n')