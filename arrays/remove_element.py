# Remove Element -> Uses a two-pointer approach to remove all occurrences of a given value in an array in-place and returns the new length of the modified array.

nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(arr, x):
    k = 0

    for i in range(len(nums)):
        if x != arr[i]:
            arr[i] = arr[k]
            k += 1

    print(nums)
    return k

print(removeElement(nums, val))