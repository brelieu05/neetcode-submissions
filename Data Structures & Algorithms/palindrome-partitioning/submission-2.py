class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        subset = []

        def backtrack(l):
            if l >= len(s):
                res.append(subset.copy())
                return

            for r in range(l + 1, len(s) + 1):
                substring = s[l:r]
                if substring == substring[::-1]:
                    subset.append(substring)
                    backtrack(r)
                    subset.pop()
            

        backtrack(0)
        return res