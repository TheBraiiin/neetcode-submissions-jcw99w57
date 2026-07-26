"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        line = []
        # intervals.sort()

        for interval in intervals:
            line.append((interval.start, 1))
            line.append((interval.end, -1))
        
        line.sort()

        count = 0
        res = 0

        for _, val in line:
            count += val 
            res = max(res, count)

        return res