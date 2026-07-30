class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        # if not prerequisites:
        #     return res
            

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

                completed.add(node)
                res.append(node)

                for nextNode in adj[node]:
                    indegrees[nextNode] -= 1
                    if indegrees[nextNode] == 0:
                        q.append(nextNode)

        return res if len(completed) == numCourses else []
