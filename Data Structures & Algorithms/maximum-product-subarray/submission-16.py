class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(2)]

        res = nums[0]

        dp[0][0], dp[1][0] = nums[0], nums[0]

        first, second = nums[0], nums[0]



        for i in range(1, n):
            # dp[0][i] = max(nums[i], nums[i] * dp[0][i-1], nums[i] * dp[1][i-1])
            # dp[1][i] = min(nums[i], nums[i] * dp[1][i-1], nums[i] * dp[0][i-1])
            temp = first
            first = max(nums[i], nums[i] * first, nums[i] * second)
            second = min(nums[i], nums[i] * second, nums[i] * temp)
            res = max(res, first)
        return res
