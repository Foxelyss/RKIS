from random import randrange

rows = 2
columns = 10

array = []

maximums = []

for x in range(columns):
    sub_array = []
    for y in range(rows):
        sub_array.append(randrange(0, 51))
    array.append(sub_array)


def max(arr):
    maximum = arr[0]
    for x in arr:
        if x > maximum:
            maximum = x
    return maximum


for y in range(columns):
    maximums.append(max(array[y]))

print("Изначальный массив: ", *array, sep='\n')
print(f"Максимумы: {maximums}")
