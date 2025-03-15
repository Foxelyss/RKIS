# Задание 6. Напишите функцию для нахождения произведения чисел, которые стоят на не
# четных местах

def multiple_even_places(lst):
    multiplication = 1
    
    for x in range(len(lst)):
        if (x+1) % 2 != 0:
            multiplication *= lst[x] 
    
    return multiplication


input_list = [12, 3, 1, 8, 1, 3, 2]
print(input_list)
print(multiple_even_places(input_list))

