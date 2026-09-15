class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def backtrack(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            
            if n not in memo:
                memo[n] = backtrack(n - 1) + backtrack(n-2)
                
            return memo[n]
        return backtrack(n)