nums = list(map(int, input("Enter array elements with spaces: ").split()))
target = int(input("Enter target: "))

for x in range(len(nums)):
    value = nums[x]

    for i in range(x, len(nums)):
        if value + nums[i] == target:
            print([x, i])
            print(f"Because nums[{x}] + nums[{i}] == {target}, we return [{x}, {i}].")
