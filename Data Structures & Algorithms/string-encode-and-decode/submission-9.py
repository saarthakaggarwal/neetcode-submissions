class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            length = len(s)
            res += "#" + str(length) + "#" + s

        return res




    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        res = []
        while i < len(s):
            if s[i] == "#":
                i += 1
                letterCount = ""
                while s[i] != "#":
                    letterCount += s[i]
                    i += 1
                
                i += 1
                letterCount = int(letterCount)
                r = ""
                for a in range(letterCount):
                    r += s[i]
                    i += 1
                res.append(r)
        return res






