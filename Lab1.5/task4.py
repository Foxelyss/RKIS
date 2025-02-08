l1 = list(map(int, input("Введите элементы массива l1 через пробел: ").split()))
l2 = list(map(int, input("Введите элементы массива l2 через пробел: ").split()))

total_list = l1 + l2

array_sorted = False
while not array_sorted:
    array_sorted = True
    for x in range(len(total_list) - 1):
        if total_list[x] > total_list[x + 1]:
            total_list[x], total_list[x + 1] = total_list[x + 1], total_list[x]
            array_sorted = False

print("Отсортированный массив:", total_list)
