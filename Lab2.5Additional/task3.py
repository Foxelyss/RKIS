# Задание 3
# Создайте класс BankAccount с приватным атрибутом balance. Реализуйте методы для депозита, снятия и проверки баланса.
# Используйте методы доступа для работы с приватным атрибутом.

class BankAccount:
    def __init__(self, balance:float):
        self.__balance = balance

    def deposit(self, amount:float):
        self.__balance = self.__balance + amount

    def withdraw(self, amount:float):
        self.__balance = self.__balance - amount

    def check_balance(self):
        return self.__balance

dummy_bank = BankAccount(1000)

print(dummy_bank.check_balance())

dummy_bank.deposit(2100)

print(dummy_bank.check_balance())

dummy_bank.withdraw(100)

print(dummy_bank.check_balance())