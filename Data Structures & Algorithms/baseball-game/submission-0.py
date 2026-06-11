class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            try:
                a = int(op)
                stack.append(a)

            except:
                if op == "+":
                    b = stack.pop()
                    c = stack.pop()
                    stack.append(c)
                    stack.append(b)
                    stack.append(b + c)
                    
                elif op == "D":
                    d = stack.pop()
                    stack.append(d)
                    stack.append(d * 2)
                else:
                    stack.pop()
            

        return sum(stack)