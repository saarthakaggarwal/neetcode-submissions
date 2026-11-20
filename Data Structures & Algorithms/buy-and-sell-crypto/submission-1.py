class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        buyPrice = float("inf")


        for p in prices:
            if p < buyPrice:
                buyPrice = p

            res = max(res, p - buyPrice)

        return res
            
