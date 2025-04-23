array = []

for x in range(14):
    array.append(int(input()))

array.append(sum(array))

for x in array:
    print(x)
