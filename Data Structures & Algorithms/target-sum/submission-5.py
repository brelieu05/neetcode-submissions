from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # @lru_cache(None)
        # def dfs(i, total):

        #     if i >= len(nums) and total == target:
        #         return 1
                
        #     if i >= len(nums):
        #         return 0


        #     add = dfs(i + 1, total + nums[i])
        #     sub = dfs(i + 1, total - nums[i])

        #     return add + sub
        # return dfs(0, 0)

        dp = defaultdict(int)

        dp[0] = 1 

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp

        return dp[target]


