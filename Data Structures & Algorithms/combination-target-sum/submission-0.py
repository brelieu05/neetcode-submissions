class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curr, total, i):
            nonlocal res

            if total > target or i >= len(nums):
                return
                
            if total == target:
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(curr, total + nums[i], i)
            curr.pop()

            dfs(curr, total, i + 1)

            
        dfs([], 0, 0)
        return res
            