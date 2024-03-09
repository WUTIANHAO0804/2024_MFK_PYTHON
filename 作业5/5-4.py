def sort_calls(file_input, file_output):
    calls_a = []  # список звонков для заместителя A
    calls_b = []  # список звонков для заместителя B

    # Чтение данных из файла
    with open(file_input, 'r') as file:
        for line in file:
            date, duration, deputy, phone = line.strip().split('\t')
            call = (date, int(duration), deputy, phone)
            if deputy == 'A':
                calls_a.append(call)
            elif deputy == 'B':
                calls_b.append(call)

    # Сортировка списков звонков по длительности в обратном порядке
    calls_a.sort(key=lambda x: x[1], reverse=True)
    calls_b.sort(key=lambda x: x[1], reverse=True)

    # Запись отсортированных звонков в файл
    with open(file_output, 'w') as file:
        for call in calls_a:
            file.write('\t'.join(map(str, call)) + '\n')
        for call in calls_b:
            file.write('\t'.join(map(str, call)) + '\n')

# Пример использования
sort_calls('the_calls.txt', 'calls.txt')