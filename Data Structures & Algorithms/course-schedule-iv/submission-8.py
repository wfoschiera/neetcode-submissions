from functools import cache


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        for dep, course in prerequisites:
            adj[course].add(dep)

        @cache
        def query(course, dependency):
            deps = adj.get(course)
            if deps is None:
                return False
            if dependency in deps:
                return True
            for dep in deps:
                if query(dep, dependency) is True:
                    return True
            return False
         
        res = []
        for dep, crs in queries:
            res.append(query(crs, dep))

        return res