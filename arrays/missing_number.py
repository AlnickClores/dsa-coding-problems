# Find the missing number in an array containing numbers from 0 to n (one number is missing)
nums = [9,6,4,2,3,5,7,0,1]

def findMissingNumber(x):
    for i in range(len(x) + 1):
        if i not in x:
            return i
    return -1
    
print("-- Find Missing Number --")
print(findMissingNumber(nums))
print()


# Find all missing numbers in a range from 0 to max value in the array
nums = [10, 7, 3, 1, 2, 6, 8]

def findMissingNumbers(x):
    x = set(x) # remove duplicates
    missing_numbers = []
    
    for i in range(max(x) + 1):
        if i not in x:
            missing_numbers.append(i)
    
    return missing_numbers
    
print("-- Find Missing Numbers --")
print(findMissingNumbers(nums))
print()