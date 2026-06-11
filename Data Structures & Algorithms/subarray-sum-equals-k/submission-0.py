class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hm = {}
        hm[0] = 1


        curSum = 0
        res = 0

        for num in nums:
            curSum += num 
            diff = curSum - k

            res += hm.get(diff, 0)
            hm[curSum] = 1 + hm.get(curSum, 0)

        return res 