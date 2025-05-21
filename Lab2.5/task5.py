# Задание 5. Напишите функцию для вычисления значения выражения (a+4b)(a−3b)+a2;

a = int(input("Введите число а:"))
b = int(input("Введите число б:"))


def calculate(a, b):
    return (a + 4 * b) * (a - 3 * b) + 2 * a


print(calculate(a, b))
