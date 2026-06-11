class Solution:

    def encode(self, strs: List[str]) -> str:
        y = ""
        for s in strs:
            x = len(s)
            y += "#"
            y += str(x)
            y += "#"
            y += s

        print(y)
        return y


    def decode(self, s: str) -> List[str]:
        y = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] != "#":
                continue
            i += 1
            x = ""
            while s[i] != "#":
                x += s[i]
                i += 1
            
            i += 1
            z = ""

            for c in range(int(x)):
                z += s[i]
                i += 1
            y.append(z)



        return y