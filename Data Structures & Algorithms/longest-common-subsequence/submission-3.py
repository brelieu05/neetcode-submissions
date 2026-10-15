from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # def recurse(idx1, idx2):
        #     if idx1 >= len(text1) or idx2 >= len(text2):
        #         return 0

        #     if text1[idx1] == text2[idx2]:
        #         return 1 + recurse(idx1 + 1, idx2 + 1)

        #     return max(recurse(idx1 + 1, idx2), recurse(idx1, idx2 + 1))
            
        
        # return recurse(0, 0)
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        print(dp)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                    continue
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])


        return dp[0][0]
