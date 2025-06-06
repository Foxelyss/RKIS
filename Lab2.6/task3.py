# Задание 3. Создайте класс Task описывающий занятие, с свойствами: DateStart, DateFinish,
# Description. Создайте список объектов Task из 5 элементов. Выведите информацию о занятии
# заканчивающемся позже всех, если таких занятий несколько, выведите первое подходящее
# под условие;
from datetime import date


class Task:
    def __init__(self, date_start: date, date_finish: date, description: str):
        self.date_start = date_start
        self.date_finish = date_finish
        self.description = description


tasks = [Task(date(2025, 1, 10), date(2025, 1, 11), "Шейпинг"),
         Task(date(2025, 2, 15), date(2025, 2, 18), "Вычисление машины тьюринга"),
         Task(date(2025, 3, 23), date(2025, 3, 23), "Конкурс Мисс Вселенная"),
         Task(date(2025, 1, 11), date(2025, 1, 12), "Фитнес"),
         Task(date(2025, 1, 24), date(2025, 1, 25), "Написание романа")]

max_finish_date = tasks[0].date_finish
max_finish_date_index = 0

for x in range(len(tasks)):
    if tasks[x].date_finish > max_finish_date:
        max_finish_date = tasks[x].date_finish
        max_finish_date_index = x

task = tasks[max_finish_date_index]

print(f"Занятие заканчивающиеся позже всех: {task.date_start} {task.date_finish} {task.description}")
