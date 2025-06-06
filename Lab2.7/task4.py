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

minimum_duration_in_minutes_index = 0
maximum_duration_in_minutes_index = 0

for x in range(len(clients)):
    if clients[x].duration_in_minutes < minimum_duration_in_minutes_index:
        minimum_duration_in_minutes_index = x
    elif clients[x].duration_in_minutes > maximum_duration_in_minutes_index:
        maximum_duration_in_minutes_index = x

minimum_duration_client = clients[minimum_duration_in_minutes_index]
maximum_duration_client = clients[maximum_duration_in_minutes_index]
print(f"FitnessCentreClient id:{minimum_duration_client.client_id} year: {minimum_duration_client.year} month: {minimum_duration_client.month} Minute duration: {minimum_duration_client.duration_in_minutes}")
print(f"FitnessCentreClient id:{maximum_duration_client.client_id} year: {maximum_duration_client.year} month: {maximum_duration_client.month} Minute duration: {maximum_duration_client.duration_in_minutes}")
