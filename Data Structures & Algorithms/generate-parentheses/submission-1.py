class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(opened, closed, parentheses):
            if opened == closed == n:
                res.append(''.join(parentheses))
                return

            if opened < n:
                parentheses.append("(")
                backtrack(opened + 1, closed, parentheses)
                parentheses.pop()
            if opened > closed:
                parentheses.append(")")
                backtrack(opened, closed + 1, parentheses)
                parentheses.pop()
            
            

        backtrack(0, 0, [])
        return res