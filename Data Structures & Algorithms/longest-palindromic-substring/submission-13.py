class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # i,j 0
        # 0  [T]

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        idx, length = 0, 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and (dp[i+1][j-1] or j - i + 1 <= 3):
                    dp[i][j] = True
                    if j - i + 1 > length:
                        idx, length = i, j - i + 1

        return s[idx : idx + length]