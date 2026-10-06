class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(combo, i, total):
            if total == target:
                res.append(combo.copy())
                return

            if total > target or i >= len(nums):
                return


            combo.append(nums[i])
            backtrack(combo, i, total + nums[i])

            combo.pop()
            backtrack(combo, i + 1, total)

        backtrack([], 0, 0)
        return res


