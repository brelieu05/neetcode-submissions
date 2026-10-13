class Solution:
    def numDecodings(self, s: str) -> int:
        encoding = {str(i + 1) : chr(ord('A') + i) for i in range(26)}
        
        dp = {}
        def recurse(i):
            if i >= len(s):
                return 1
            
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0

            ways = recurse(i + 1)
            
            if i + 1 < len(s) and s[i: i + 2] in encoding:
                ways += recurse(i + 2)

            dp[i] = ways
            return dp[i]

        return recurse(0)