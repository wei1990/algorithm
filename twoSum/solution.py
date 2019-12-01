class Solution: 
    def twoSum(self, nums, target):
        k = 0
        for i in nums:
            k = k + 1
            if target - i in nums[k:]:
                return [k - 1, nums[:].index(target - i)]
