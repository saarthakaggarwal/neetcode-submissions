class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        res = []

        

        for i, n in enumerate(nums):
            l ,r = i + 1, len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            
            while l < r:
                sumOfNums = nums[i] + nums[l] + nums[r]
                if sumOfNums < 0: 
                    l += 1
                elif sumOfNums > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l > 0 and nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
        