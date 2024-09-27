x = int(input("Enter number to reverse: "))

x_inversed = 0

while x > 0:
    x_inversed *= 10
    x_inversed += (x % 10)
    x //= 10

print("Reversed number is", x_inversed)
