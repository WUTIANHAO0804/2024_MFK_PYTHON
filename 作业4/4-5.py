import csv

# Функция для расчета вклада
def calculate_deposit(amount, period, rate):
    monthly_rate = rate / 12 / 100  # Переводим годовую ставку в месячную и в десятичную форму
    total_months = period * 12  # Общее количество месяцев

    results = []  # Список для хранения результатов
    for month in range(1, total_months + 1):
        interest = amount * monthly_rate  # Начисление процентов за месяц
        amount += interest  # Капитализация процентов
        results.append((month, amount, interest))

    return results

# Чтение входных данных
input_data = input("Введите сумму вклада, срок в годах и процентную ставку через пробел: ")
amount_str, period_str, rate_str = input_data.split()
amount = float(amount_str)  # Преобразование в float для суммы вклада
period = int(period_str)  # Преобразование в int для срока в годах
rate = float(rate_str)  # Преобразование в float для процентной ставки

# Выполнение расчета
deposit_data = calculate_deposit(amount, period, rate)

# Сохранение результатов в файл
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Месяц", "Сумма на вкладе", "Начисление"])  # Заголовок таблицы
    for row in deposit_data:
        writer.writerow([f"{row[0]}", f"{row[1]:.2f}", f"{row[2]:.2f}"])  # Запись данных с округлением до двух знаков

print("Расчет выполнен и сохранен в файле output.csv.")