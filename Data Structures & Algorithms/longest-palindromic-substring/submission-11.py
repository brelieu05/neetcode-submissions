class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] 

        maxIdx, maxLength = 0, 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i + 1 <= 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j - i + 1) > maxLength:
                        maxIdx = i
                        maxLength = j - i + 1
        return s[maxIdx : maxIdx + maxLength]