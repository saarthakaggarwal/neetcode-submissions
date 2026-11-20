class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = set(nums)
        res = 0

        for n in nums:
            if n - 1 in x:
                continue
            else:
                y = n
                curr = 0 
                while y in x:
                    curr += 1
                    y += 1

                res = max(curr, res)

        return res