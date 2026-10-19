from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache
        def recurse(i, j):
            if j < 0:
                return i < 0

            if p[j] == "*":
                preceding = p[j - 1]

                # Option 1: Match zero occurrences
                skip = recurse(i, j - 2)

                # Option 2: Match one or more occurrences
                match = (
                    i >= 0
                    and (preceding == "." or s[i] == preceding)
                    and recurse(i - 1, j)
                )

                return skip or match

            if i < 0:
                return False

            if p[j] == "." or s[i] == p[j]:
                return recurse(i - 1, j - 1)

            return False

        return recurse(len(s) - 1, len(p) - 1)