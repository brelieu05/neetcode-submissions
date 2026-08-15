class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        # loop through
            # calculate time
            # append time to stack
            # while stack is not monotonically decreasing
                # pop

        for p, s in pair:
            time = ((target - p) / s)


            stack.append(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

