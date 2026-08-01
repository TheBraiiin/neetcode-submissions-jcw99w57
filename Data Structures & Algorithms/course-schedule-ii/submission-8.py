class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = defaultdict(list)
        indegrees = [0] * numCourses

        for end, start in prerequisites:
            adj[start].append(end)
            indegrees[end] += 1

        q = deque()
        completed = set()

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

                while q:
                    node = q.popleft()
                    if node in completed:
                        continue
                    completed.add(node)
                    res.append(node)
                    for nextNode in adj[node]:
                        indegrees[nextNode] -= 1
                        if indegrees[nextNode] <= 0:
                            q.append(nextNode)

        return res if len(res) == numCourses else []

        
