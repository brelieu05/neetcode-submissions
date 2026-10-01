class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(combo, total, i):
            if total == target:
                res.append(combo.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                combo.append(nums[j])
                dfs(combo, total + nums[j], j)
                combo.pop()

        dfs([], 0, 0)
        return res