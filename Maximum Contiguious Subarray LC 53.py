#LC 
#LC 53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = nums[0]
        maxSum = nums[0]
        i = 1
        while(i<len(nums)):
            currentMax = max(currentMax + nums[i], nums[i])
            maxSum = max(maxSum, currentMax, nums[i])
            i += 1
        return maxSum