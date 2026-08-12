class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0, 0)] # (num, index)
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if stack:
                while stack and stack[-1][0] < temperatures[i]:
                    num, index = stack.pop()
                    res[index] = i - index
                stack.append((temperatures[i], i))
        return res

            