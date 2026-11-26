class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 0 -> numCourses-1
        adj = defaultdict(list)
        for dep, course in prerequisites:
            adj[course].append(dep)

        {1: [0]}
        # {c: [b], b: [a]}  logo, {c: [b, a]}
        
        def query(course, dependency, visited):
            deps = adj.get(course)
            print(deps)
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
        print(f"{adj=}")
        for dep, crs in queries:
            res.append(query(crs, dep, set()))

        return res