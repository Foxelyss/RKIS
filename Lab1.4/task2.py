import random

start = int(input("Введите начало диапазона для случайных чисел генерации массива:"))
end = int(input("Введите конец диапазона для случайных чисел генерации массива:"))


def generate_array_of_random_numbers(start, end):
    arr = []
    for x in range(10):
        arr.append(random.randrange(start, end+1))
    return arr


print(generate_array_of_random_numbers(start, end))
