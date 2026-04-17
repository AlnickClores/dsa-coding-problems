# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

nums = [0,0,1,1,1,2,2,3,3,4] # 5 = [0,1,2,3,4,_,_,_,_,_]

def removeDuplicates(x):
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1

    return l

print(removeDuplicates(nums))