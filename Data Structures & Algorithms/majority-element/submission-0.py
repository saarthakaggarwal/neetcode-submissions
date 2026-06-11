from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hm = defaultdict(int)

        for n in nums:
            hm[n] += 1

        for key in hm:
            if hm[key] > (len(nums) // 2):
                return key