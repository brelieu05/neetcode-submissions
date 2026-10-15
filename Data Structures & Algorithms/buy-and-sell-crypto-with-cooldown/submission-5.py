class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # memo = {}
        # def dfs(i, bought):
        #     if i >= len(prices):
        #         return 0

        #     if (i, bought) in memo:
        #         return memo[(i, bought)]
            
        #     buy = 0
        #     if not bought:
        #         buy = dfs(i + 1, True) - prices[i]
        #     else:
        #         sell = prices[i] + dfs(i + 2, False)
        #         skip = dfs(i + 1, True)
        #         buy += max(sell, skip)

        #     skip = dfs(i + 1, False)

        #     memo[(i, bought)] = max(buy, skip)
        #     return max(buy, skip)

        # return dfs(0, False)

        n = len(prices)
        dp = [[0] * (n + 1) for _ in range(2)]

        dp[0][0], dp[1][0], dp[0][1] = float('-inf'), 0, (-1) * prices[0]


        for i in range(2, n + 1):
            buy = dp[1][i-2] - prices[i-1]
            sell = dp[0][i-1] + prices[i-1]

            dp[0][i] = max(buy, dp[0][i-1])
            dp[1][i] = max(sell, dp[1][i-1])

        return dp[-1][-1]



