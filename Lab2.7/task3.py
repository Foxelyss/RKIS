# Задание 3. Дана целочисленная последовательность. Извлечь из нее все положительные
# двузначные числа, отсортировав их по возрастанию;


import random

lst = [random.randrange(1, 30) - 15 for _ in range(10)]

new_lst = []
for x in lst:
    if x // 10 > 0:
        new_lst.append(x)

new_lst.sort()

print(lst)
print(new_lst)
