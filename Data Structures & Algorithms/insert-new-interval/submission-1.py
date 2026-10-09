class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        # for loop through every interval
            # if newInterval comes before current interval, then we know we don't need to merge anything ever since the intervals are all in order
                # return interval + res[i:]
            # if newInterval comes after, we can just append the current interval since that one is not being merged. will deal with merging for the subsequent iteration

            # if interval can be merged
                # update newInterval since we might be able to merge a future interval
        # now newInterval is guaranteed to come last since if it was in the middle the first if statement would've returned first, so we res.append(newInterval)
        

        for i in range(len(intervals)):
            newStart, newEnd = newInterval
            start, end = intervals[i]

            if newEnd < start:
                res.append(newInterval)
                return res + intervals[i:]

            elif newStart > end:
                res.append(intervals[i])
            else:
                newInterval = [min(start, newStart), max(end, newEnd)]
        res.append(newInterval)
        return res

