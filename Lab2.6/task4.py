# Задание 4. Дана целочисленная последовательность, содержащая как положительные, так
# и отрицательные числа. Вывести ее первый положительный элемент и последний
# отрицательный элемент;
import random

lst = [random.randrange(1, 10) - 5 for _ in range(10)]

print("Массив", lst)
print("Первый положительный и отрицательный элементы:")

positive_first = False
negative_first = False

for x in lst:
    if x > 0 and not positive_first:
        positive_first = True
        print(x)
    elif x < 0 and not negative_first:
        negative_first = True
        print(x)
