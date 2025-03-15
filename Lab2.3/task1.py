# Задание 1. Выведите на экран названия текущих дня недели и месяца, и свое имя. Каждое
# слово должно быть в отдельной строке;

import datetime

date = datetime.datetime.now().strftime('%A\n%B')
print(f"{date}\nСтепан\nFoxelyss!")
