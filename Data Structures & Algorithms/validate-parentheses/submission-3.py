class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbols = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if stack and c in symbols and stack[-1] == symbols[c]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0