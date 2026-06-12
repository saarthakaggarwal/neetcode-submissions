class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)


        stack = [] #[index, temperature]


        for i, temp in enumerate(temperatures):
            print(stack, res)
            while stack and stack[-1][1] < temp:
                index, t = stack.pop()
                res[index] = i - index

            stack.append([i, temp])


        return res
