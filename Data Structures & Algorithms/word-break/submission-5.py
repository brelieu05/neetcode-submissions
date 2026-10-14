from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # @lru_cache
        # def dfs(i):
        #     if i == len(s):
        #         return True
        #     for word in wordDict:
        #         if word in s[i:i + len(word)]:
        #             if dfs(i + len(word)):
        #                 return True
        #     return False
        # return dfs(0)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True



        for i in range(n):
            if dp[i]:
                for word in wordDict:
                    if s.startswith(word, i):
                        dp[i + len(word)] = True
        return dp[-1]

