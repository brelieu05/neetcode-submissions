class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, bought):
            if i >= len(prices):
                return 0

            if (i, bought) in memo:
                return memo[(i, bought)]
            
            buy = 0
            if not bought:
                buy = dfs(i + 1, True) - prices[i]
            else:
                sell = prices[i] + dfs(i + 2, False)
                skip = dfs(i + 1, True)
                buy += max(sell, skip)

            skip = dfs(i + 1, False)

            memo[(i, bought)] = max(buy, skip)
            return max(buy, skip)

        return dfs(0, False)