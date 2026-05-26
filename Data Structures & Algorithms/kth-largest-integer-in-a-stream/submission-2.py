class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        min_heap = nums
        heapq.heapify(nums)

        while len(min_heap) > self.k:
            heapq.heappop(min_heap)

        self.min_heap = min_heap

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)


        return self.min_heap[0]
        
