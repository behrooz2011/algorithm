"""
15. 3Sum
Medium
22.4K
2K
Companies
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        for k in range(len(nums)-2):
            # print('k:',k)
            obj = {}
            #nums[i] + nums[j] = -nums[k]
            for i in range(k+1,len(nums)):
                if -nums[k]-nums[i] not in obj:
                    obj[nums[i]] = [i,-nums[k]-nums[i]]
                else:
                    sol = [nums[i],nums[k],nums[obj[-nums[k]-nums[i]][0]]]
                    sol.sort()
                    # print("sol: ",sol)
                    if sol not in res:res.append(sol)
        # print("res",res)
        return res