"""
3. Longest Substring Without Repeating Characters
Medium

Companies
Given a string s, find the length of the
 longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""
def largestSub(s):
    arr =[]
    maxLength=0
    for i in range(len(s)):
        if s[i] not in arr:
            arr.append(s[i])
        else:
            maxLength = max(maxLength,len(arr))
            # clip the array when a repetitive element comes up
            # print("arr.index: ",arr.index(s[i]))
            arr = arr[arr.index(s[i])+1:]
            arr.append(s[i]) # add the new value after clipping the array
    return max(maxLength,len(arr))
print(largestSub("pwwkgewlfetw"))
print(largestSub("aaaa"))
print(largestSub("abccefghj"))
print(largestSub("aabcd"))
print(largestSub("aabaabkbb"))
