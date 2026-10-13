# Напишите функцию, которая заполняет массив случайным числам
# в диапазоне, указанном пользователем. Функция должна принимать 
# два аргумента: начало диапазона и его конец, возвращать получившийся массив чисел

import random

start = int(input("Введите начало диапазона для случайных чисел генерации массива:"))
end = int(input("Введите конец диапазона для случайных чисел генерации массива:"))


def generate_array_of_random_numbers(start, end):
    arr = []
    for x in range(10):
        arr.append(random.randrange(start, end+1))
    return arr


print(generate_array_of_random_numbers(start, end))
