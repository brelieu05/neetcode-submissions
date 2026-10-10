class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        combo = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9": "wyxz"}
        res = []

        def backtrack(i, p):
            if len(p) == len(digits):
                res.append(p)
                return

            if i >= len(digits):
                return


            for char in combo[digits[i]]:
                p += char
                backtrack(i + 1, p)
                p = p[:-1]



        backtrack(0, "")
        return res
