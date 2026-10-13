# Если число m больше числа n, то выведите на экран 
# «Number m > n», Если число m меньше числа n, то выведите на 
# экран «Number m < n», в противном случае выведите сообщение «The numbers are equal»

m = int(input("Enter number m: "))
n = int(input("Enter number n: "))

if m > n:
    print("Number m > n")
elif m < n:
    print("Number m < n")
else:
    print("The numbers are equal")
