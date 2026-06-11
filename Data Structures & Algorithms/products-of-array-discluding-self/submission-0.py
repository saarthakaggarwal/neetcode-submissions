class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        runningMultiplier = 1
        output = [1] * len(nums)

        for i, n in enumerate(nums):
            output[i] *= runningMultiplier
            runningMultiplier *= n
        
        
        runningMultiplier = 1
        for i, n in enumerate(reversed(nums)):
            output[len(nums) - 1 - i] *= runningMultiplier
            runningMultiplier *= n

            
        print(output)
        return output

