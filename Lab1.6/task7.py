x = int(input())


def check_value_for_decrease(a = 0):
    array_value = list(map(int, list(str(a))))
    for x in range(len(array_value) - 1):
        if array_value[x]  < array_value[x + 1]:
            return False
    return True


print("Число - ", x)
if check_value_for_decrease(x):
    print("Цифры в числе идут с убыванием")
else:
    print("Цифры в числе не идут с убыванием")
