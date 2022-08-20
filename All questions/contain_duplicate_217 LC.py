#contain duplicate
class Solution:    
    def containsDuplicate(self, nums):
        obj = {}
        for i in range(len(nums)):
            if nums[i] in obj:
                return True
            else:
                obj[nums[i]]=i
        return False


#Solution2 
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) < len(nums)