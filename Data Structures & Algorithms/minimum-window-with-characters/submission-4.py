class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need, have = {}, {}

        for c in t:
            need[c] = need.get(c, 0) + 1


        l, found = 0, 0
        res = [0, 0]
        minResLen = float("inf")


        for r in range(len(s)):
            have[s[r]] = have.get(s[r], 0) + 1
            if s[r] in need and have[s[r]] == need[s[r]]:
                found += 1

            while found == len(need):
                have[s[l]] = have.get(s[l]) - 1
                if r - l + 1 < minResLen:
                    minResLen = r - l + 1
                    res = [l, r]
                if s[l] in need and have[s[l]] < need[s[l]]:
                    found -= 1
                l += 1

        if minResLen == float("inf"):
            return ""

        return s[res[0] : res[1] + 1]



