# Write a function to find the longest common prefix string amongst an array of strings

strs = ["flower","flow","flight"] # -> "flo"

def longestCommonPrefix(strs):
    common_prefix = ""

    for i in range(len(strs[0])):
        reference = strs[0][i]

        for word in strs:
            if i == len(word) or word[i] != reference:            
                return common_prefix
        
        common_prefix += word[i]

    return common_prefix

    

print(longestCommonPrefix(strs))