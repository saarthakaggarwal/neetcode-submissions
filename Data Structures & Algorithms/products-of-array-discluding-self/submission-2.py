import copy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        runningProduct = 1
        for i, n in enumerate(nums):
            res[i] *= runningProduct
            runningProduct *= nums[i]


        runningProduct = 1
        for i, n in enumerate(nums[::-1]):
            res[len(nums) - 1 - i] *= runningProduct
            runningProduct *= n

        return res