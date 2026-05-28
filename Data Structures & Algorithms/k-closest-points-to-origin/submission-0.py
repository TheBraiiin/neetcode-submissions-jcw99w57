class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = self.distance(points, point[0], point[1])
            heapq.heappush(heap,(dist, point))

        res = []
        while k > 0:
            p, point = heapq.heappop(heap)
            res.append(point)
            k -= 1
        
        return res

    def distance(self, points, x1, y1):
        return math.sqrt(x1 ** 2 + y1 ** 2)