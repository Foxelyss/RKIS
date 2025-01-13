# Перед студентом стоит задача: на вход функции sieve() поступает список
# целых чисел. В результате выполнения этой функции будет получен кортеж
# уникальных элементов списка в обратном порядке.

user_list = list(map(int, input().split()))


def sieve(lst):
    unique_elements = []
    for x in set(lst):
        if lst.count(x) != 1:
            unique_elements.append(x)

    unique_elements.sort(reverse=True)

    return tuple(unique_elements)


print("Уникальность:", sieve(user_list))
