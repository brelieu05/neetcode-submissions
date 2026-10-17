from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache
        def recurse(s1, s2, s3):
            if not s3:
                return not s1 and not s2

            if not s1:
                return s2 == s3

            if not s2:
                return s1 == s3
            
            if not s1 and not s2 and not s3:
                return True
            
            result = False

            if s1[0] == s3[0]:
                result = result or recurse(s1[1:], s2, s3[1:])

            if s2[0] == s3[0]:
                result = result or recurse(s1, s2[1:], s3[1:])

            return result

        return recurse(s1, s2, s3)
            