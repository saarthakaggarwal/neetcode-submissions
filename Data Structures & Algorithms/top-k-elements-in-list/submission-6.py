class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        array = [[] for _ in range(len(nums) + 1)]
        hm = {}


        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        
        for key, value in hm.items():
            array[value].append(key)


        curr = len(nums) - 1
        j = 0
        res = []
        while j < k:
            for n in array[curr]:
                res.append(n)
                j += 1

            curr -= 1

        return res