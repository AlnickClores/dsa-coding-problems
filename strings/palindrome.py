# palindrome -> a word, phrase, or sequence that reads the same backward as forward

word = 123321 # -> True

def isPalindrome(x):
    x = str(x).lower()

    left = 0
    right = len(x) - 1

    while left <= right:
        if x[left] != x[right]:
            return False
        
        left += 1
        right -= 1

    return True

print(isPalindrome(word))