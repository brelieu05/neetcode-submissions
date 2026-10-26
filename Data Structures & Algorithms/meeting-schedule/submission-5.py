"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)
        times = []

        for interval in intervals:
            
            for time in times:
                if time.start <= interval.start < time.end or time.start < interval.end <= time.end :
                    return False

            times.append(interval)

        return True
