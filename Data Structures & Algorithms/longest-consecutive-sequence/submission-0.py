class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setForNums = set(nums)
        res = 0
   
        for n in nums:
            if n - 1 in nums:
                continue
            curNum = n
            curLength = 1
            while curNum + 1 in setForNums:
                curNum += 1
                curLength += 1

            res = max(curLength, res)

        return res