class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hm = {}

        for letter in s:
            if letter in hm:
                hm[letter] += 1
            else:
                hm[letter] = 1

        hm2 = {}
        for letter in t:
            if letter in hm2:
                hm2[letter] += 1
            else:
                hm2[letter] = 1

        
        return hm == hm2