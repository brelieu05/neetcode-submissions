class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recurse(n):
            if n in memo:
                return memo[n]
                
            if n <= 2:
                return n

            memo[n] = recurse(n-2) + recurse(n-1)
            return memo[n]


        return recurse(n)