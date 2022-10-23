""" 20. Valid Parentheses
Easy
16.3K
824
Companies
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false """

class Solution:
    def isValid(self, s: str) -> bool:
        arr= []
        negValue = ['{', '[', '(']
        obj = {
            '[':-10, ']':10, 
            '{':-20, '}':20,
            '(':-30, ')':30
        }
        for i in range(len(s)-1, -1, -1):
            if len(arr) == 0:
                arr.append(s[i])
            else:
                if arr[0] in negValue:
                    return False
                else:
                    if obj[s[i]] + obj[arr[0]] == 0:
                        arr.pop(0)
                    else:
                        arr.insert(0,s[i])
        return (len(arr) == 0)