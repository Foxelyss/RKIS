import datetime

days = ["Понедельник", "Вторник", "Среда",
        "Четверг", "Пятница", "Суббота", "Воскресенье"]
months = ["январь", "февраль", "март", "апрель", "май", "июнь",
          "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

month = datetime.datetime.today().month
day = datetime.datetime.today().day

print(f"Сегодня {days[day]}, {months[month]} месяц. Степан")
