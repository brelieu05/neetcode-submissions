class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dfs(i, amount):
            if amount == 0:
                return 0
            
            if i >= len(coins):
                return float('inf')

            if (i, amount) in memo:
                return memo[(i, amount)]

            choice1 = 1 + dfs(i, amount - coins[i]) if amount >= coins[i] else float('inf')
            choice2 = dfs(i + 1, amount)

            memo[(i, amount)] = min(choice1, choice2)
            return memo[(i, amount)]

        res = dfs(0, amount)
        return res if res < float('inf') else -1


        