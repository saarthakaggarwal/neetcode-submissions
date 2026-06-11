class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        x = set()
        l, r = 0, 0
        longest = 0
        
        while r < len(s):
            if s[r] not in x:
                x.add(s[r])
                r += 1
                longest = max(longest, r - l)
            else:
                while s[l] != s[r]:
                    x.remove(s[l])
                    l += 1
                x.remove(s[l])
                l += 1
        return longest
