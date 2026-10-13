# Сгенерируйте массив(случайной длины, до 25-ти элементов) 
# из чисел расположенных по убыванию, которые делятся на 3 без остатка

from random import randint

array = []

for x in range(randint(1, 25)):
    array.append((25 - x) * 3)

print("Массив чисел :", array)
