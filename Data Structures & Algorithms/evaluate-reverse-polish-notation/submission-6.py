class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                stack.append(val1 + val2)
            elif token == "-":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                stack.append(val2 - val1)  
            elif token == "*":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                stack.append(val1 * val2)
            elif token == "/":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                stack.append(int(val2 / val1))
            else:
                stack.append(int(token))
        return stack[0]