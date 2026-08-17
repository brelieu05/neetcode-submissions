class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if len(stack) >= 2 and token == "+":
                stack.append(stack.pop() + stack.pop())
            elif len(stack) >= 2 and token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif len(stack) >= 2 and token == "*":
                stack.append(stack.pop() * stack.pop())
            elif len(stack) >= 2 and token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))

        return stack[0]