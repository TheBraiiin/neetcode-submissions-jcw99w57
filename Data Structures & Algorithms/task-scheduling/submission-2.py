class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskc = defaultdict(int)
        for task in tasks:
            taskc[task] += 1

        heap = [(p, key) for key, p in taskc.items()]
        heapq.heapify_max(heap)

        q = deque()

        time = 0

        while heap or q:
            if not q:
                p, key = heapq.heappop_max(heap)
                taskc[key] -= 1
                if taskc[key] > 0:
                    q.append((key, time + n))
                time += 1
            elif not heap:
                key, tasktime = q[0]
                if tasktime == time:
                    q.popleft()
                    heapq.heappush_max(heap, (taskc[key], key))
                time += 1
            else:
                while q and q[0][1] == time:
                    key, tasktime = q.popleft()
                    heapq.heappush_max(heap, (taskc[key], key))
                p, key = heapq.heappop_max(heap)
                taskc[key] -= 1
                if taskc[key] > 0:
                    q.append((key, time + n))
                time += 1
                
        return time



        
        

         