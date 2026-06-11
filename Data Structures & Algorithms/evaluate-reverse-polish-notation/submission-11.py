class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                print(stack)
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a = stack.pop() 
                b = stack.pop()
                c = b - a
                stack.append(c)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a = stack.pop() 
                b = stack.pop()
                c = int(b / a)
                stack.append(c)
            else:
                stack.append(int(token))

        return stack.pop()