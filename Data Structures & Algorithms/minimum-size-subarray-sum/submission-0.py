class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 100
        l, r = 0, 0
        currSum = 0

        while r < len(nums):
            currSum += nums[r]

            while currSum >= target:
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l += 1
            
            r += 1

        if res == 100:
            return 0
        return res

