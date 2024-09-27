
def find_odd_items_multiplication(array):
    multiplication = 1
    for x in range(len(array)):
        if x % 2 != 0:
            multiplication *= array[x]

    return multiplication
