import itertools

# Генерируем все возможные комбинации значений True и False для x1, x2 и x3
combinations = list(itertools.product([False, True], repeat=3))

# Проверяем каждую комбинацию
for x1, x2, x3 in combinations:
    # Вычисляем значение логического высказывания для текущей комбинации
    result = ((not x1 and x2 and not x3) or (not x1 and x2 and x3) or (x1 and not x2 and not x3))
    # Если результат истинен, выводим текущую комбинацию
    if result:
        print(x1, x2, x3)