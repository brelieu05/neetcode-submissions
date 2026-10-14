from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        # @lru_cache(None)
        # def dfs(i, currSum):
        #     if currSum == target:
        #         return True

        #     if currSum > target:
        #         return False

        #     if i == len(nums):
        #         return False

        #     take = dfs(i + 1, currSum + nums[i])
        #     skip = dfs(i + 1, currSum)

        #     return take or skip
        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            for s in range(target + 1):
                # Skip nums[i - 1]
                dp[i][s] = dp[i - 1][s]

                # Take nums[i - 1]
                if s >= nums[i - 1]:
                    dp[i][s] = (
                        dp[i][s] or
                        dp[i - 1][s - nums[i - 1]]
                    )
                
        return dp[-1][-1]