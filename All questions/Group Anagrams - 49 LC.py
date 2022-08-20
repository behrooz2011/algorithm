# 49. Group Anagrams
# Medium

# 7071

# 257

# Add to List

# Share
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
def g(strs):
    res=[]
    obj={}
    for i in range(len(strs)):
        if ''.join(sorted(strs[i])) not in obj:
            obj[''.join(sorted(strs[i]))]=[strs[i]]
            for j in range(i+1, len(strs)):
                if ''.join(sorted(strs[i])) == ''.join(sorted(strs[j])):
                    obj[''.join(sorted(strs[i]))].append(strs[j])
            print("sorted elements of the string array:\t",''.join(sorted(strs[i])))
            res.append(obj[''.join(sorted(strs[i]))])
        else:
            continue
    return(res)
print(g(["eat","tea","tan","ate","nat","bat"]))