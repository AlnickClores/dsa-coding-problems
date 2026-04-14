# Anagram -> Check if two strings are anagrams (same characters with same frequency, ignoring spaces and case)
str1 = "earth"
str2 = "heart"

def isAnagram(x, y):
    x = x.replace(" ", "").lower()
    y = y.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    # { char : frequency }
    xCount, yCount = {}, {}
    
    for i in range(len(x)):
        xCount[x[i]] = 1 + xCount.get(x[i], 0)
        yCount[y[i]] = 1 + yCount.get(y[i], 0)
    
    for i in xCount:
        if xCount[i] != yCount.get(i, 0):
            return False
    
    return True

print("-- Anagram Checker --")
print(isAnagram(str1, str2))
print()