# Выведите на экран названия текущих дня недели и месяца,
# и свое имя. Каждое слово должно быть в отдельной строке

import datetime

today = datetime.datetime.today()

print(f"Сегодня {today.strftime("%A %B")} месяц. Степан")
