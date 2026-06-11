class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.curMin = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(self.curMin)
        self.curMin = min(self.curMin, val)

    def pop(self) -> None:
        self.curMin = self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curMin
        
