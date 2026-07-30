class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        adj = defaultdict(list)

        for end, start in prerequisites:
            adj[start].append(end)

            visiting = set()
            completed = set()

            def dfs(course):
                if course in visiting:
                    return False
                if course in completed:
                    return True

                visiting.add(course)

                for nextCourse in adj[course]:
                    if not dfs(nextCourse):
                        return False
                
                visiting.remove(course)
                completed.add(course)

                return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return len(completed) == numCourses