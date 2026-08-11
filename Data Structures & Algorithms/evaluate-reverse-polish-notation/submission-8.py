class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if len(stack) >= 2 and t == "+":
                stack.append(stack.pop() + stack.pop())
            elif len(stack) >= 2 and t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif len(stack) >= 2 and t == "*":
                stack.append(stack.pop() * stack.pop())
            elif len(stack) >= 2 and t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(t))
        return stack[0]
        