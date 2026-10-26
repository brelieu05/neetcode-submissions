class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        stack = (-1, float('inf'))
        res = 0

        for interval in intervals:
            start, end = interval

            if stack and start < stack[1]:
                res += 1

                if end < stack[1]:
                    stack = (start, end)
            else:
                stack = (start, end)
        return res - 1