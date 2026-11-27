class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval

        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][1] < start:
                l = mid + 1
            else:
                r = mid - 1
        r = l
        while r < len(intervals) and intervals[r][0] <= end:
            start = min(start, intervals[r][0])
            end = max(end, intervals[r][1])
            r += 1


        intervals[l:r] = [[start, end]]
        return intervals