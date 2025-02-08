# Создайте целочисленную коллекцию. Добавьте в нее 10 случайных чисел.
# Выведите в консоль минимальный элемент коллекции;

import random

int_list = [random.randint(1, 20) for x in range(10)]

print(min(int_list))
