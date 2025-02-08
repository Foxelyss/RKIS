# Напишите функцию для нахождения минимального элемента массива. Функция
# принимает целочисленный массив и возвращает число

def minimal(lst: [int]):
    minimal = lst[0]

    for x in lst:
        if minimal > x:
            minimal = x

    return minimal


a = [123, 9, 3, 57, 23, 123.-1, -5, 100]

print(minimal(a))
