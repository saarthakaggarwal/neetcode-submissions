class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curMin = 1000

        for p in prices:
            if p < curMin:
                curMin = p
            else:
                res = max(res, p - curMin)

        return res