class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        #find peak


        l, r = 0, mountainArr.length() - 1
        peak = -1

        while l <= r:
            mid = (l + r) // 2

            i, j, k = mountainArr.get(mid - 1), mountainArr.get(mid), mountainArr.get(mid + 1)
            
            if i <= j <= k:
                l = mid + 1
            elif i >= j >= k:
                r = mid - 1
            else:
                peak = mid
                break
        
        #check left 

        l, r = 0, peak
        ret = -1 

        while l <= r:
            mid = (l + r) // 2
            m = mountainArr.get(mid)
            if m > target:
                r = mid - 1
            elif m < target:
                l = mid + 1
            else:
                return mid


        #check right 

        l, r = peak, mountainArr.length() - 1

        while l <= r:
            mid = (l + r) // 2
            m = mountainArr.get(mid)

            if m > target:
                l = mid + 1
            elif m < target:
                r = mid - 1
            else:
                return mid

        return -1

