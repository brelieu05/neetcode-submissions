class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0] * n for _ in range(m)]

        # for i in range(m):
        #     dp[i][0] = 1

        # for j in range(n):
        #     dp[0][j] = 1

        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i][j-1] + dp[i-1][j]
        # return dp[-1][-1]

        memo = {}
        def recurse(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
                
            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            right = recurse(i, j + 1)
            down = recurse(i + 1, j)

            memo[(i, j)] = right + down

            return right + down

        return recurse(0, 0)

            