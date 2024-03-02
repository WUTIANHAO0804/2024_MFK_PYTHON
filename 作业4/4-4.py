import math

def find_smallest_exceeding_member(b1, q, a):
    if q <= 1 and b1 <= a:
        return "Такого члена не существует"
    n = math.ceil((math.log(a / b1) / math.log(q)) + 1)
    return n

# Пример использования функции с одновременным вводом значений
input_str = input()
b1, q, a = map(float, input_str.split())

print(find_smallest_exceeding_member(b1, q, a))