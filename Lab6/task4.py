a = int(input("Введите число а: "))
b = int(input("Введите число б: "))


def max_of_two(a, b):
    if a > b:
        return a
    return b


print(f"Максимальное из двух чисел: {max_of_two(a, b)}")
