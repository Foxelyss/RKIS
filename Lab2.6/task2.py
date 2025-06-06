# Задание 2. Создайте класс User с свойствами Login и Password. Создайте список объектов
# User из 5 элементов. Выведите из этого списка пользователя с определенными логином и
# паролем;

class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password


users = [User("foxelyss", "123ASD!"), User("tails", "4654!"),
         User("sonic", "123ASD@"), User("knuckles", "456!"),
         User("longvehicle", "321!")]

user = "foxelyss"

for user in users:
    if user.login == user:
        print(f"User @{user.login} Password {user.password}")
