# Задание 5
# Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм, 
# а с помощью метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной “kg” она 
# реализовала методы set_kg() - для задания нового значения килограммов, get_kg()  - для вывода текущего значения кг. 
# Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для задания и вывода значений. 
# Помогите ей переделать класс с использованием функции property() и свойств-декораторов. Код приведен ниже.

class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.20462

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, value):
        self.__kg = value


elephant = KgToPounds(148.6)

print("Вес в кг:", elephant.kg)
print("Вес в фунтах:", elephant.to_pounds())

elephant.kg = 325
print("Вес в кг:", elephant.kg)
print("Вес в фунтах:", elephant.to_pounds())
