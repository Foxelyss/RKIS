nums = list(map(int, input("Введите элементы массива через пробел: ").split()))
target = int(input("Введите цель: "))

target_index = 0

for x in range(len(nums)):
    if target > nums[x]:
        target_index = x + 1

print(target_index)
