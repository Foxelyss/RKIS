from random import randrange

random_array = [randrange(-10, 11) for x in range(10)]


def find_odd_items_multiplication(array):
    multiplication = 1
    for x in range(len(array)):
        if x % 2 != 0:
            multiplication *= array[x]

    return multiplication


print("Массив чисел:", random_array)
print("Умножение элементов с нечётными номерами:",
      find_odd_items_multiplication(random_array))
