class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mheap = Counter(tasks)
        mheap = [val for val in mheap.values()]
        heapq.heapify_max(mheap)

        # processing queue
        q = deque()
        time = 0
        while q or mheap:
            time += 1

            if not mheap:
                time = q[0][1] 
            else:
                cnt = heapq.heappop_max(mheap) - 1
                if cnt > 0:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                tskcnt, tsktime = q.popleft()
                heapq.heappush_max(mheap, tskcnt)

        return time

         

         