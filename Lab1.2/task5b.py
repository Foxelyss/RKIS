# б) сумму всех целых чисел от a до 500 (значение a вводится с клавиатуры; a<500)

a = int(input("Введите начальное число до 500: "))

all_numbers = list(range(a, 501))
sum_of_all_numbers = sum(all_numbers)

print(f"Сумма всех чисел {a} до 500 включительно равна:", sum_of_all_numbers)
