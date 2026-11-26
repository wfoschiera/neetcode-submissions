class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for dep, course in prerequisites:
            adj[course].append(dep)

        def query(course, dependency, visited):
            deps = adj.get(course)
            if deps is None:
                return False
            if dependency in deps:
                return True
            for dep in deps:
                if dep in visited:
                    return False
                visited.add(dep)
                if query(dep, dependency, visited) is True:
                    return True
            return False
         
        res = []
        for dep, crs in queries:
            res.append(query(crs, dep, set()))

        return res