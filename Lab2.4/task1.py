# Создайте массив размерностью 15. С помощью цикла for заполните массив
# случайными числами. Выведите элементы массива используя цикл foreach;

from random import randint

array = []

for x in range(15):
    array.append(randint(1, 100))

for x in array:
    print(x)
