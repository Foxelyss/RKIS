x = int(input())


def check_value_for_decrease(a):
    first_value = 0
    decreasing = True
    while a > 0:
        first_value = a % 10
        a //= 10
        if first_value > (a % 10) and a > 0:
            decreasing = False
    return decreasing


print("Число - ", x)
if check_value_for_decrease(x):
    print("Цифры в числе идут с убыванием")
else:
    print("Цифры в числе не идут с убыванием")
