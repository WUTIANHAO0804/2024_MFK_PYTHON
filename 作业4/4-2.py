from fractions import Fraction

# Ввод данных
a_n, a_d = map(int, input().split())
b_n, b_d = map(int, input().split())
c_n, c_d = map(int, input().split())

# Создание объектов Fraction
a = Fraction(a_n, a_d)
b = Fraction(b_n, b_d)
c = Fraction(c_n, c_d)

# Вычисление выражения
result = b / a + b / (a + c) - c / (c - a)

# Преобразование результата в число с плавающей точкой и его округление
result_float = float(result)
print(f"{result_float:.4f}")