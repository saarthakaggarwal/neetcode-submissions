from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
       hashmap = defaultdict(int)
       freqCount = [[] for _ in range(len(nums) + 1)]

       for n in nums:
            hashmap[n] += 1
        
       for key, value in hashmap.items():
            freqCount[value].append(key)

       j = 0
       res = []
       for arr in reversed(freqCount):
        for arr in reversed(freqCount):
            if j >= k:
                break

            for n in arr:
                res.append(n)
                j += 1

        return res