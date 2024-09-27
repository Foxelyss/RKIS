size = int(input("Введите число, над которым будет проводиться операция: "))
print("Введите режим работы с числом:\n1 для перевода килобайт в байты,\n2 для перевода байт в килобайты")
mode = int(input("Режим: "))


def convert_to_bytes(size_in_kilobytes):
    return size_in_kilobytes * 1024


def convert_to_kilobytes(size_in_bytes):
    return size_in_bytes // 1024


if mode == 1:
    print(f"Число {size} килобайт в байтах равно", convert_to_bytes(size))
elif mode == 2:
    print(f"Число {size} байт в килобайтах равно", convert_to_kilobytes(size))
else:
    print("Операции не существует")
