a = int(input("Введите первую сторону прямоугольника: "))
b = int(input("Введите вторую сторону прямоугольника: "))
c = int(input("Введите сторону квадрата: "))


def calculate_square_quantity_for_rectangle(width, length, cube_width):
    return (width * length) // (cube_width ** 2)


print(f"Количество квадратов которых можно вырезать из этого прямоугольника = {calculate_square_quantity_for_rectangle(a, b, c)}")
