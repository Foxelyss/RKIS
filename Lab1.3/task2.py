a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

m = 0

if a > b and a > c:
    m = a
elif b > a and b > c:
    m = b
else:
    m = c

print("Максимальное число равно", m)
