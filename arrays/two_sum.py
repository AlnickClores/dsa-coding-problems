# Find two numbers in a list that sum to a target value and return their indices.

arr = [2,7,11,15]
target = 18

def twoSumBrute(nums, x):
    # Brute force solution
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == x:
                return [i, j]
    return -1

def twoSumHash(nums, x):
    # Hashmap lookup solution ( better way )
    # { number : index }
    numbers = {}

    for i in range(len(nums)):
        complement = x - nums[i]

        if complement in numbers:
            return [numbers[complement], i]

        numbers[nums[i]] = i

    return -1

print("Brute Force Solution:", twoSumBrute(arr, target))
print("Hashmap Solution:", twoSumHash(arr, target))