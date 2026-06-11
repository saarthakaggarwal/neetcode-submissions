class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l , r = 0, len(s) - 1
        
        def checkAfterReplacement(l, r, s):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                    continue 
                return False

            return True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue 
            
            return checkAfterReplacement(l + 1, r, s) or checkAfterReplacement(l, r - 1, s)
        
        
        return True