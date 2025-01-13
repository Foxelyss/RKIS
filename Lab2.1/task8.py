# Дана дата в следующем формате: '2025-12-31'
# Преобразуйте эту дату в следующий словарь:
# {
#  'year' : '2025',
#  'month': '12',
#  'day' : '31',
# }

date_string = '2007-01-10'

date_list = date_string.split("-")

date_dict = {
    "year": date_list[0],
    "month": date_list[1],
    "day": date_list[2]
}

print("Для даты:", date_string)
print("Словарь выглядит:", date_dict)
