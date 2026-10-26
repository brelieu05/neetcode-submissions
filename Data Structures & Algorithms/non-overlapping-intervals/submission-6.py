class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        currEnd = float('-inf')
        res = 0

        for interval in intervals:
            start, end = interval

            if start < currEnd:
                res += 1

                if end < currEnd:
                    currEnd = end
            else:
                currEnd = end
        return res