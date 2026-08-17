import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calcTime(k):
            total_time = 0
            for p in piles:
                total_time += math.ceil((p / k))

            return total_time <= h

        l, r = 1, max(piles)


        while l < r:
            mid = (l + r) // 2
            print(mid)
            if calcTime(mid):
                r = mid
            else:
                l = mid + 1

        return r

