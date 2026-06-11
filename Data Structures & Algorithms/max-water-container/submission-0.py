class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            width = r - l 
            leftHeight, rightHeight = heights[l], heights[r]
            maxHeight = min(leftHeight, rightHeight)
            res = max(width * maxHeight, res)

            if leftHeight >= rightHeight:
                r -= 1
            else:
                l += 1

        return res
            