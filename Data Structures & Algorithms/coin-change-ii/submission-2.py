from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        @lru_cache(None)
        def dfs(i, total):
            if total == amount:
                return 1

            if i >= len(coins) or total > amount:
                return 0
            
            take = dfs(i, total + coins[i])
            take += dfs(i + 1, total)

            return take

        return dfs(0, 0)



            