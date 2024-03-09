with open('weights.txt', 'r') as file:
    data = [line.strip().split() for line in file]

# Сортировка игроков по убыванию веса
data.sort(key=lambda x: float(x[1]), reverse=True)

# Разделение игроков на две команды
team1 = [player[0] + ' ' + player[1] for index, player in enumerate(data) if index % 2 == 0]
team2 = [player[0] + ' ' + player[1] for index, player in enumerate(data) if index % 2 != 0]

# Запись результатов в файл team.txt
with open('team.txt', 'w') as file:
    for player in team1[:11]:
        file.write(player + '\n')
    for player in team2[-11:]:
        file.write(player + '\n')