class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = defaultdict(list)

        for end, start in prerequisites:
            adj[start].append(end)

        visiting = set()
        completed = set()
        def dfs(course):
            nonlocal res
            if course in visiting:
                return False
            if course in completed:
                return True
            
            visiting.add(course)

            for nextCourse in adj[course]:
                if not dfs(nextCourse):
                    return False
                
            res.append(course)
            visiting.remove(course)
            completed.add(course)
            return True

        for c in range(numCourses):
            if c not in completed:
                if not dfs(c):
                    return []
                        
        return list(reversed(res))

        # 0 - 1 - 3
        # |     /
        # |   /
        # | /
        # 2