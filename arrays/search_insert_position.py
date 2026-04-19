# Search Insert Position -> Uses binary search to find the target in a sorted array, and if it’s not found, returns the index where it should be inserted to keep the array sorted.

nums = [1,3,5,6]
target = 7

def searchInsertPosition(arr, x):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + r // 2

        if x == arr[mid]:
            return mid
        
        if x > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return l


print(searchInsertPosition(nums, target))