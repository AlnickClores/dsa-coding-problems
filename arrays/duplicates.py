# Find the first duplicate pair in an array (return the indices of the first matching duplicate)
nums =  [1,2,3,4,2,5]

def findDuplicate(x):
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            if x[i] == x[j]:
                return i, j
    return -1

print("-- Find Duplicate --")
print(findDuplicate(nums))
print()


# Find all numbers and store the list of indexes where each number appears
nums =  [1,2,3,1,4,1,4,2,2,1,4,5,5,6,6] # 1:4, 2:3, 3:1, 4:3, 5:2, 6:2

def findDuplicates(x):
    # { number : [list of indexes] }
    duplicates_indexes = {}
    # { number : frequency }
    duplicates_frequency = {}
    
    for i in range(len(x)):
        if x[i] not in duplicates_indexes:
            duplicates_indexes[x[i]] = [i]
        else:
            duplicates_indexes[x[i]].append(i)

    for i in range(len(x)):
        duplicates_frequency[x[i]] = 1 + duplicates_frequency.get(x[i], 0)
        
    print("Duplicate Indexes: ", duplicates_indexes)
    print("Duplicate Frequency: ", duplicates_frequency)

print("-- Find Duplicates --")
findDuplicates(nums)
print()