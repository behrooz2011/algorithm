"""
424. Longest Repeating Character Replacement
Medium
6.3K
245
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""

""" https://www.youtube.com/watch?v=gqXU1UyA8pk """
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res= 0
        l =0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            if (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res