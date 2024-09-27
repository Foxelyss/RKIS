from random import randint

array = []

for x in range(randint(1, 25)):
    array.append((25 - x) * 3)

print(array)
