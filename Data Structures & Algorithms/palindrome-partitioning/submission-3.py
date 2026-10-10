class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(l):
            if l >= len(s):
                res.append(part.copy())
                return

            for r in range(l, len(s)):
                substring = s[l:r + 1]
                if substring == substring[::-1]:
                    part.append(substring)
                    backtrack(r + 1)
                    part.pop()

        backtrack(0)
        return res