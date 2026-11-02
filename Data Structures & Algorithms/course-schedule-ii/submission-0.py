from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(set)

        for course, pre in prerequisites:
            adj_list[course].add(pre)

        res = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for pre in adj_list[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res        