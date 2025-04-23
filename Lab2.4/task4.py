# Напишите функцию, которая будет преобразовывать введенную
# пользователем дату (за текущий год) к следующему виду;
# Input: 01.09.2021
# Output: Среда, 1 Сентября, 2021 год

from datetime import datetime

inputted_date = datetime.strptime(input(), "%d.%m.%Y")


def format_date(date: datetime):
    if datetime.today().year != date.year:
        return ""

    return inputted_date.strftime("%A, %-d %B, %Y год")


print(format_date(inputted_date))
