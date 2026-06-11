class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []

        mapping = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }


        for par in s:
            if par in mapping:
                if not stack or stack.pop() != mapping[par]:
                    return False
                continue
            
            stack.append(par)

        return not stack