class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            length = len(s)
            res += f"#{length}#{s}"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            i += 1
            number = ""
            while s[i] != "#":
                number += s[i]
                i += 1

            i += 1
            number = int(number)
            r = ""
            for j in range(number):
                r += s[i]
                i += 1

            res.append(r)

        return res    

