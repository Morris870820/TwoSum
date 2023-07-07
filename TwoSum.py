def twoSum(nums, target):
    temp = {}
    for num in range(len(nums)):
        num1 = nums[num]
        num2 = target - num1
        if num2 in temp:
            return [temp[num2], num]
        else:
            temp[num1] = num

# 測試
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)