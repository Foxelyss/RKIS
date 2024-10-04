x = int(input("Введите число для поиска: "))
array = list(map(int, input("Введите элементы массива через пробел: ").split()))

element_found = False
for i in array:
    if x == i:
        element_found = True
        break

if element_found:
    print("Элемент имеется")
else:
    print("Такого элемента нет")
