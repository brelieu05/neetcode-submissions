class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = {}

        def recurse(idx1, idx2):

            if (idx1, idx2) in dp:
                return dp[(idx1, idx2)]
                
            if idx2 >= len(t):
                return 1

            if idx1 >= len(s):
                return 0

            
            if s[idx1] == t[idx2]:
                dp[(idx1, idx2)] = recurse(idx1 + 1, idx2 + 1) + recurse(idx1 + 1, idx2)
                return dp[(idx1, idx2)]
            else:
                dp[(idx1, idx2)] = recurse(idx1 + 1, idx2)
                return dp[(idx1, idx2)]

        return recurse(0, 0)

        



        