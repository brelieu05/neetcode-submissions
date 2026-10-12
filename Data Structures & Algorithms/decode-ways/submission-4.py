

class Solution:
    def numDecodings(self, s: str) -> int:
        encoding = {str(i + 1) : chr(65 + i) for i in range(0, 26)}
        n = len(s)
        memo = {}

        def dfs(i):
            if i >= len(s):
                return 1

            if s[i] == "0":
                return 0
            
            if i in memo:
                return memo[i]

            ways = 0

            if s[i] in encoding:
                ways += dfs(i + 1)

            if i + 1 < n and s[i:i+2] in encoding:
                ways += dfs(i + 2)

            memo[i] = ways
            return memo[i]

        return dfs(0)