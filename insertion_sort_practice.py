nums = [4, 2, 3, 1]
i = 1
while i < len(nums):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] >= key:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key
    i += 1
print(nums)