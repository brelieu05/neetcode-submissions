class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        stack = []
        res = 0

        for interval in intervals:
            start, end = interval

            if stack and (stack[-1][0] <= start < stack[-1][1] or stack[-1][0] <= end < stack[-1][1]):
                res += 1
                if end < stack[-1][1]:
                    stack.pop()
                    stack.append(interval)
            else:
                stack.append(interval)
        return res