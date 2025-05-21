# Задание 2
# Создайте базовый класс Animal с методом speak.
# Затем создайте два подкласса Dog и Cat, которые наследуют от Animal и переопределяют метод speak.
# Создайте объекты этих классов и вызовите метод speak.
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('Woof Woof')

class Cat(Animal):
    def speak(self):
        print("Meow Meow")


murzik = Cat()
murzik.speak()

laika = Dog()
laika.speak()