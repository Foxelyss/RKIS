# Задание 2. Петя успевает по математике лучше всех в классе, поэтому учитель задал ему
# сложное домашнее задание, в котором нужно в заданном наборе целых чисел найти сумму
# всех положительных элементов, затем найти где в заданной последовательности
# находятся максимальный и минимальный элемент и вычислить произведение чисел,
# расположенных в этой последовательности между ними. Так же известно, что
# минимальный и максимальный элемент встречаются в заданном множестве чисел только
# один раз и не являются соседними. Напишите функцию, которая примет массив и вернет
# два числа (сумму положительных элементов и произведение чисел, расположенных между
# минимальным и максимальным элементами);

array_of_numbers = [10, 0, 1, -2, 3, 4, 5, 6, 7, 8, 9]


def solve_question(arr):
    sum_of_positive_numbers = 0
    for number in arr:
        if number > 0:
            sum_of_positive_numbers += number

    min_number_index = arr.index(min(arr))
    max_number_index = arr.index(max(arr))
    if min_number_index <= max_number_index:
        numbers_between_min_max = arr[min_number_index+1:max_number_index]
    else:
        numbers_between_min_max = arr[max_number_index+1:min_number_index]

    multiplication_of_numbers_min_max = 1

    for number in numbers_between_min_max:
        multiplication_of_numbers_min_max *= number

    return sum_of_positive_numbers, multiplication_of_numbers_min_max


print(solve_question(array_of_numbers))
