class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sarray = [0] * 26
        tarray = [0] * 26


        for i in range(len(s)):
            sarray[ord(s[i]) - ord("a")] += 1
            tarray[ord(t[i]) - ord("a")] += 1


        return sarray == tarray