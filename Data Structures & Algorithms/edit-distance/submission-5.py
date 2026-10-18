class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}
        def recurse(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                memo[(i, j)] = recurse(i + 1, j + 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = min(1 + recurse(i, j + 1), 1 + recurse(i + 1, j), 1 + recurse(i + 1, j + 1))
                return memo[(i, j)]

            

        return recurse(0, 0)