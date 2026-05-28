class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)

            p = abs(s1 - s2)

            if p > 0:
                heapq.heappush_max(stones, p)

        return stones[0] if stones else 0
