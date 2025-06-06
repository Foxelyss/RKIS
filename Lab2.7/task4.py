# Задание 4. Создать класс описывающий фитнес-центр с свойствами: Код клиента, Год,
# Номер месяца, Продолжительность занятия. Создайте список объектов класса фитнес-центр
# из 5 элементов. Вывести информацию о самом продолжительном и самом коротком занятиях;

class FitnessCentreClient:
    def __init__(self, client_id: int, year: int, month: int, duration_in_minutes: int):
        self.client_id = client_id
        self.year = year
        self.month = month
        self.duration_in_minutes = duration_in_minutes


clients = [
    FitnessCentreClient(1, 2007, 1, 123),
    FitnessCentreClient(1, 2008, 4, 13),
    FitnessCentreClient(1, 2014, 5, 321),
    FitnessCentreClient(1, 2018, 1, 123),
    FitnessCentreClient(1, 2023, 3, 13),
    FitnessCentreClient(1, 2023, 3, 321-14)
]

years = {}

for x in clients:
    if x.year not in years:
        years[x.year] = x.duration_in_minutes
    else:
        years[x.year] += x.duration_in_minutes



