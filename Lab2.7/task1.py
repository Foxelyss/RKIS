# Задание 1. Дана строковая последовательность. Найти сумму длин всех строк, входящих в
# данную последовательность;
import random
import string

strings = ["".join(random.sample(string.ascii_uppercase, k=random.randrange(2,19))) for _ in range(10)]

print(strings)

length_of_all = sum([len(string) for string in strings])

print(length_of_all)