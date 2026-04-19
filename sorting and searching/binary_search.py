# Binary Search -> Uses two pointers (left and right) to repeatedly divide a sorted list in half to find the target.

nums = [1,2,3,4,5,6,7,8,9,10]
target = 7

def binarySearch(arr, x):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if target == arr[mid]:
            return mid
        
        if target > arr[mid]:
            l = mid + 1
        else:
            r = mid -1

    return -1

print(binarySearch(nums, target))