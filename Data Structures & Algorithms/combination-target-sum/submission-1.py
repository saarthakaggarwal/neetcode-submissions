class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()

        def recurse(i, curSum, sol):
            if curSum > target:
                return
            if curSum == target:
                res.append(sol.copy())
                return


            for j in range(i, len(nums)):
                sol.append(nums[j])
                recurse(j, curSum + nums[j], sol)
                sol.pop(-1)
                


        recurse(0, 0, [])
        return res