x = int(input("Введите число для поиска: "))
array = list(map(int, input("Введите элементы массива через пробел: ").split()))

if x in array:
    print("Элемент имеется")
else:
    print("Такого элемента нет")
