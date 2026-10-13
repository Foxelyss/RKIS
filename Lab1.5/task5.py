# Дан отсортированный массив различных целых чисел
# и какое-то значение target, верните индекс, если target найдено. 
# Если нет, верните индекс, где target могло бы быть, если бы оно было вставлено по порядку

nums = list(map(int, input("Введите элементы массива через пробел: ").split()))
target = int(input("Введите цель: "))

target_index = 0

for x in range(len(nums)):
    if target > nums[x]:
        target_index = x + 1

print(target_index)
