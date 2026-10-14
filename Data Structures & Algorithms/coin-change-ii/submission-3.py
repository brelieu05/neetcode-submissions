class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}
        def dfs(i, total):
            if total == amount:
                return 1

            if i >= len(coins) or total > amount:
                return 0

            if (i, total) in memo:
                return memo[(i, total)]
            
            take = dfs(i, total + coins[i])
            take += dfs(i + 1, total)

            memo[(i, total)] = take
            return memo[(i, total)]

        return dfs(0, 0)



            