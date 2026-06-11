class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k

        while lo < hi:
            mid = (hi + lo) // 2

            if abs(x - arr[mid]) > abs(x - arr[mid + k]):
                lo = mid + 1
            else:
                hi = mid 

        return arr[lo: lo + k]