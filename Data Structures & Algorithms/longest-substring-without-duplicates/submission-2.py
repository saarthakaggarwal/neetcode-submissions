class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        x = set()
        i, j = 0, 0
        res = 0
        
        while j < len(s): 
            while s[j] in x:
                x.remove(s[i])
                i += 1
            
            x.add(s[j])
            res = max(res, j - i + 1)
            j += 1

        return res