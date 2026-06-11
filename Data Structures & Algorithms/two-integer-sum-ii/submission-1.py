class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1


        while l < r:
            num1, num2 = numbers[l], numbers[r]
            t = num1 + num2

            if t < target:
                l += 1
            elif t > target:
                r -= 1
            else:
                return [l + 1, r + 1]
