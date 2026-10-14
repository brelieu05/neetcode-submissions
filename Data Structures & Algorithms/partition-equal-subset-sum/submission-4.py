from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        @lru_cache(None)
        def dfs(i, currSum):
            if currSum == target:
                return True

            if currSum > target:
                return False

            if i == len(nums):
                return False

            take = dfs(i + 1, currSum + nums[i])
            skip = dfs(i + 1, currSum)

            return take or skip


        return dfs(0, 0)