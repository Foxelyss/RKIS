# Напишите функцию, которая определяет является ли число a делителем числа
# b. Функция должна вернуть логическое значение true или false;

def is_devider(number, devider):
    return number % devider == 0


print(is_devider(20, 10))
print(is_devider(20, 11))
