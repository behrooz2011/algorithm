class Two:
    def twoSum(self,nums,target):
        obj = {}
        for i in range(len(nums)):
            if nums[i] in obj:
                return ([i,obj[nums[i]]])
            else:
                obj[target - nums[i]] = i
        return []
