#two sum with two pointer
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        newNum = nums.copy()
        nums.sort()
        i = 0
        j = len(nums)-1
        while(i<j):
            if nums[i] + nums[j] == target:
                if nums[i] != nums[j]:
                    return [newNum.index(nums[i]),newNum.index(nums[j])]
                else:
                    last_occ =len(newNum) - 1 - newNum[::-1].index(nums[i])
                    #last occurance of nums[i]
                    return [newNum.index(nums[i]),last_occ]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return []
