class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        def calcDays(k):
            tdays = 1
            cursum = 0

            for w in weights:
                if cursum + w > k:
                    tdays += 1
                    cursum = 0

                cursum += w 

            return tdays <= days

        l, r = max(weights), sum(weights)


        while l < r:
            mid = (l + r) // 2

            if calcDays(mid):
                r = mid
            else:
                l = mid + 1


        return l