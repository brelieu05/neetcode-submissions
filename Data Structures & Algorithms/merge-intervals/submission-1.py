class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for start, end in intervals:
            top_start, top_end = stack[-1] if stack else [float('inf'), float('-inf')]
            if top_start <= start <= top_end or top_start <= end <= top_end:
                stack[-1] = [min(start, top_start), max(end, top_end)]
            else:
                stack.append([start, end])

        return stack
                

