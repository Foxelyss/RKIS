# Задание 5. Напишите функцию, для нахождения количества положительных чисел в
# массиве. Функция принимает массив чисел и возвращает количества положительных чисел
# в массиве;

def positive_numbers_of_list(lst):
    positive_list = []

    for x in lst:
        if x > 0:
            positive_list.append(x)
    
    return positive_list

print(positive_numbers_of_list([-1,-2,3,-5,0,9,2]))
