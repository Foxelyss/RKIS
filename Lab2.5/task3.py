# Задание 3. Сформируйте возрастающий массив из случайных четных чисел;

import random

random_array = [random.randint(1 + i*10, 10 + i*10) for i in range(10)]

print(random_array)