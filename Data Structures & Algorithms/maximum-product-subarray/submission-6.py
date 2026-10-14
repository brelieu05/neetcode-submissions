class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0, 0] for _ in range(n)]

        dp[0][0], dp[0][1] = nums[0], nums[0]

        res = nums[0]

        for i in range(1, n):
            valMin = dp[i - 1][0] * nums[i]
            valMax = dp[i - 1][1] * nums[i]
            dp[i][0] = max(nums[i], valMin, valMax)
            dp[i][1] = min(nums[i], valMin, valMax)
            res = max(res, dp[i][0])

        return res