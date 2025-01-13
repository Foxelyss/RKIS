#  Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется
# создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи
# будут типом int), а в качестве значений – количество этих чисел в имеющейся
# последовательности. Для построения словаря создайте функцию count_it(sequence),
# принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто
# встречаемых чисел.

import random

string = str(random.randrange(0, 30000000000))


def count_it(sequence):
    all_numbers = set(sequence)
    number_quantity = {}

    for x in all_numbers:
        number_quantity[int(x)] = sequence.count(x)

    while len(number_quantity) > 3:
        minimal = min(number_quantity.values())
        for x in number_quantity:
            if number_quantity[x] == minimal:
                del number_quantity[x]
                break

    return number_quantity


print(string)
print(count_it(string))
