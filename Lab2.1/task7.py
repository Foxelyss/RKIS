import re

# Дан список со строками. Оставьте в этом списке только те строки, которые
# начинаются на http://.
strings = [
    "Ты бы ещё консервных банок насобирал!",
    "Братья Стругацкие \"Пикник на обочине\"",
    "http:/chess.com",
    "Есть книги про метро 2033, но серия игр популярнее...",
    "http://МалоКтоЗнает.Но/Я/Не/Ссылка/Но/Я/Пройду/Через/Фильтр",
    "http://foxelyss.github.io"
]

query = re.compile("^(http:\/\/)")

for x in strings.copy():
    if query.match(x) is None:
        strings.remove(x)

print(strings)