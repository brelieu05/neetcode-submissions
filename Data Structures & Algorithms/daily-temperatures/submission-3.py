class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        # create as monotonic decreasing stack (temp, index)

        # loop through
            # append to stack
            # if len(stack) > 2 and stack[-2] < stack[-1]:
                # pop
                # res[i] = index - stack[-2][index]

        for i in range(len(temperatures)):

            while stack and stack[-1][0] < temperatures[i]:
                temp, index = stack.pop()
                res[index] = i - index

            stack.append((temperatures[i], i))

        return res