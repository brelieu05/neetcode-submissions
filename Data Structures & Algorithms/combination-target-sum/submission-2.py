class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(combo, total, i):
            nonlocal res

            if total > target or i >= len(nums):
                return

            if total == target:
                res.append(combo.copy())
                return

            # take
            combo.append(nums[i])
            dfs(combo, total + nums[i], i)

            # skip
            combo.pop()
            dfs(combo, total, i + 1)



        dfs([], 0, 0)
        return res