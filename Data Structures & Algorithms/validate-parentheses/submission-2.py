class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {"]" : "[", "}" : "{", ")" : "("}
        stack = []

        for c in s:
            if stack and c in symbols and symbols[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
            print(stack)
        return len(stack) == 0