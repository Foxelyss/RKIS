# Задание 2. Дана целочисленная последовательность. Извлечь из нее все положительные
# числа;

import random

lst = [random.randrange(1, 10) - 5 for _ in range(10)]

new_lst = []
for x in lst:
    if x > 0:
        new_lst.append(x)

print(lst)
print(new_lst)
