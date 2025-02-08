multidimensional_array = [
    [[1, 2, 4], [5, 7, 8], [9, 9, 4]],
    [[6, 3, 5], [7, 4, 2], [9, 5, 6]],
    [[7, 3, 4], [8, 7, 5], [8, 3, 4]],
]

print("Массив равен: ", *multidimensional_array, sep="\n")

for z in range(3):
    for y in range(3):
        print(
            f"Мин. точка имеет коорд-ты x={min(multidimensional_array[z][y])} y={y} z={z}")
