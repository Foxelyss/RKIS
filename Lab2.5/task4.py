# Задание 4. Дана строка. Если она начинается на «abc», то замените их на «www», иначе
# добавьте в конец строки «zzz»;

string = input()

if string.startswith("abc"):
    string = string.replace("abc", "www")
else:
    string = string + "zzz"

print(string)