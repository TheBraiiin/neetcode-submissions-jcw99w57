"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        heap = []
        intervals.sort(key=lambda interval:interval.start)

        res = 0
        for interval in intervals:
            while heap and interval.start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, interval.end)
            res = max(res, len(heap))

        return res

                # [5, 10], [15, 20], [0, 40], [50, 100]
