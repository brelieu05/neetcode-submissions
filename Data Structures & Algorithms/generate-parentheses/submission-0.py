class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(opened, closed, curr):
            if opened == closed == n:
                res.append(''.join(curr))
                return
            
            if opened < n:
                # add open
                curr.append("(")
                backtrack(opened + 1, closed, curr)
                curr.pop()
            if opened > closed:
                # add closed
                curr.append(")")
                backtrack(opened, closed + 1, curr)
                curr.pop() # why do we need this last curr.pop()?

        backtrack(0, 0, [])
        return res
