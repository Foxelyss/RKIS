# С помощью конструкции try..catch, обработайте участки кода в которых могут
# возникнуть исключения
# Напишите enum для математических операций (+, -, *, /). Создайте функцию,
# которая будет принимать 2 числа и операцию. Внутри функции создайте switch, который
# будет содержать case для каждой операции. Функция должна возвращать 4 значения
# (firstNumber, secondNumber, operation, result);

from enum import Enum


class MathemathicalOperation(Enum):
    PLUS = 0
    MINUS = 1
    MULTIPLICATION = 2
    DIVISION = 3


def calculate_operation(a: float, b: float, operation: MathemathicalOperation) -> tuple:
    result = 0

    if not isinstance(a, (float, int, complex)) or not isinstance(a, (float, int, complex)) or\
            operation not in MathemathicalOperation:
        raise TypeError("Неправильные типы данных на входе")

    if operation is MathemathicalOperation.PLUS:
        result = a+b
    elif operation is MathemathicalOperation.MINUS:
        result = a-b
    elif operation is MathemathicalOperation.MULTIPLICATION:
        result = a*b
    elif operation is MathemathicalOperation.DIVISION:
        result = a/b
    else:
        raise Exception("Операция не определена!")

    return (a, b, operation, result)


try:
    print(calculate_operation(12, 3.4, MathemathicalOperation.DIVISION))
except Exception as a:
    print(a)

try:
    print(calculate_operation(12, 0, MathemathicalOperation.DIVISION))
except ZeroDivisionError as a:
    print(a)

try:
    print(calculate_operation(12, 3.4, 123))
except TypeError as a:
    print(a)

try:
    print(calculate_operation("12", "3.4", MathemathicalOperation.DIVISION))
except TypeError as a:
    print(a)
