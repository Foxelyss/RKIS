# Задание 4
# Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент
# при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
# а иначе отобразится следующая фраза: «Обычная газировка».

class Soda:
    def __init__(self, special_ingredient:str = None):
        self.special_ingredient = special_ingredient

    def show_my_drink(self):
        if self.special_ingredient is None:
            print("Обычная газировка")
        else:
            print(f"Газировка и {self.special_ingredient}")

a = Soda("Лайм")
a.show_my_drink()

b = Soda()
b.show_my_drink()

