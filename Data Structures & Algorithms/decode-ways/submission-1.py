from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        encoding = {str(i + 1) : chr(65 + i) for i in range(0, 26)}
        n = len(s)


        @lru_cache
        def dfs(i):
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            ways = dfs(i + 1)

            if i + 1 < len(s) and s[i:i+2] in encoding:
                ways += dfs(i + 2)

            return ways

        return dfs(0)