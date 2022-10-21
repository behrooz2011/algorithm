"""49. Group Anagrams
Medium
12.2K
376
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        arr = []
        for i in range(len(strs)):
            arr.append({"name": ''.join(sorted(strs[i])), "indx":i})
        # print(arr)
        arr.sort(key=lambda x:x["name"])
        print("arr: ",arr)
        newArr=[]
        for i in range(len(arr)):
            if len(newArr) == 0:
                newArr.append(strs[arr[i]["indx"]] )
            else:
                if ''.join(sorted(newArr[0])) == ''.join(sorted(strs[arr[i]["indx"]])):
                    newArr.append(strs[arr[i]["indx"]])
                else:
                    newArr.sort()
                    res.append(newArr)
                    newArr = []
                    newArr.append(strs[arr[i]["indx"]])
        newArr.sort()
        res.append(newArr)
        return res