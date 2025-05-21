# Задание 1
# Создайте простой класс Car, который будет представлять автомобиль.
# Класс должен иметь атрибуты для марки, модели и года выпуска автомобиля.
# Затем создайте объект этого класса и выведите его атрибуты на экран

class Car:
    def __init__(self, factory:str,model:str,year:int):
        self.factory = factory
        self.model = model
        self.year = year

skoda_actavia = Car("Skoda","Actavia",2014)

print(f"Машина {skoda_actavia.factory} {skoda_actavia.model} произведена {skoda_actavia.year}")

