# Linear Search -> checks each element one by one from start to end until the target is found.

nums = [1,2,3,4,5,6,7,8,9,10]
target = 6

def linearSearch(arr, x):
    for i in range(len(arr)):
        if x == arr[i]:
            return i
        
print(linearSearch(nums, target))