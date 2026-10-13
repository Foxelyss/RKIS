# Найдите сумму и произведение цифр, введенного натурального числа. Например, 
# если введено число 325, то сумма его цифр равна 10 (3+2+5), а произведение 30 (3*2*5)

a = int(input("Введите число: "))

nums = []

while a > 0:
    nums.append(a % 10)
    a //= 10

summary = sum(nums)
multiplication = 1

for x in nums:
    multiplication *= x

print(f"Сумма всех цифр числа равна {
      summary} , а произведение равно {multiplication}")
