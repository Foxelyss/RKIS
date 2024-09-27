def a(a):
    last_value = 9
    good = True
    while a > 0:
        last_value = a % 10
        a //= 10
        if a % 10 > last_value:
            good = False
    return good
