distance_in_meters = int(input("Введите расстояние в метрах: "))
distance_in_kilometers = int(input("Введите расстояние в километрах: "))

if distance_in_meters < distance_in_kilometers * 1000:
    print(f"Наименьшее расстояние равно {distance_in_meters} м.")
elif distance_in_meters > distance_in_kilometers * 1000:
    print(f"Наименьшее расстояние равно {distance_in_kilometers} км.")
else:
    print("Расстояния равны")