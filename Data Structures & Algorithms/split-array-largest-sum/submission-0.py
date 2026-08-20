class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        

        def canSplit(largest):
            sarray = 1
            curSum = 0

            for num in nums:
                curSum += num
                if curSum > largest:
                    sarray += 1
                    if sarray > k:
                        return False
                    curSum = num

            return True




        l, r = max(nums), sum(nums)

        while l < r:
            mid = (l + r) // 2

            if canSplit(mid):
                r = mid
            else:
                l = mid + 1

        return r