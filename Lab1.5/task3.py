x = int(input("Введите число "))

a = x
x_inversed = 0

while a > 0:
    x_inversed *= 10
    x_inversed += (a % 10)
    a //= 10

if x == x_inversed:
    print("true")
else:
    print("false")
