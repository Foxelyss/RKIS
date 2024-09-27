from random import randrange

arr = [randrange(-100, 101) for x in range(10)]

negative_values = 0
positive_values = 0

zero_values = 0

for x in arr:
    if x < 0:
        negative_values += 1
    elif x > 0:
        positive_values += 1
    else:
        zero_values += 1

print(f"Элементы массива {arr}")
print(f"Количество отрицательных чисел: {negative_values}")
print(f"Количество положительных чисел: {positive_values}")
print(f"Количество нулевых чисел: {zero_values}")
