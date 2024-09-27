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
