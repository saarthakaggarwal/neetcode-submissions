class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        x = set()
        i, j = -1, 0
        res = 0
        
        while j < len(s): 
            while s[j] in x:
                i += 1
                x.remove(s[i])
                
            
            x.add(s[j])
            res = max(res, j - i)
            j += 1

        return res