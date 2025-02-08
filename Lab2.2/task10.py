# Добавляйте новые элементы в список до тех пор, пока пользователь не
# отправит пустую строку. Выведите в консоль самый короткий и самый длинный элементы
# списка;

string = input()

strings = []

shortest_string = string
longest_string = string

while string != "":
    strings.append(string)
    string = input()

for string in strings:

    shortest_string = string if len(
        shortest_string) > len(string) else shortest_string
    longest_string = string if len(string) > len(
        longest_string) else longest_string

print(f"Самый длинный элемент:{longest_string}")
print(f"Самый короткий элемент:{shortest_string}")
