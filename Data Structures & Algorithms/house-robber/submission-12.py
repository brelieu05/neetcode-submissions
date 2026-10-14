class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        #  0. 1. 2  3, 4
        # [0, 0, 0, 0, 0]
        #  0. 1. 1. 1. 3

        for i in range(2, n + 1):
            dp[i] = max(dp[i-2] + nums[i - 1], dp[i-1])

        return dp[-1]

