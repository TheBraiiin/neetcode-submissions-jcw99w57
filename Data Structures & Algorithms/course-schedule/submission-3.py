class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        indegrees = [0] * numCourses
        adj = defaultdict(list)
        for end, start in prerequisites:
            adj[start].append(end)
            indegrees[end] += 1

        q = deque()

        completed = set()
        for c in range(numCourses):
            if indegrees[c] == 0:
                q.append(c)

                while q:
                    node = q.popleft()
                    if node in completed:
                        continue

                    for nextNode in adj[node]:
                        if nextNode not in completed:
                            indegrees[nextNode] -= 1
                            if indegrees[nextNode] <= 0:
                                q.append(nextNode)

                    completed.add(node)

        return len(completed) == numCourses

                    
                