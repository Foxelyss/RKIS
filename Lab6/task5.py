from random import randrange

random_array = [randrange(-10, 11) for x in range(10)]


def positive_values_from_array(array):
    positives = 0
    for x in array:
        if x > 0:
            positives += 1
    return positives


print(f"Массив чисел: {random_array}")
print("Из данного массива положительных чисел: ",
      positive_values_from_array(random_array))
