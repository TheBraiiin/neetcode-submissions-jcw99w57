"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: (x.start, x.end))
        heap = []
        res =  0
        for interval in intervals:
            if heap and interval.start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, interval.end)
            res = max(res, len(heap))
            
        return res
            
        # (0,50),(10,60), (20,70),(30,80),(40,90),(50,100),(60,110),(70,120),(80,130),(90,140),(100,150)