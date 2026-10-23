from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False

            if pre_map[crs] == []:
                return True

            visit.add(crs)

            for pre in pre_map[crs]:
                if dfs(pre) is False: 
                    return False
            visit.remove(crs)
            pre_map[crs] = []
            return True

        for crs in range(numCourses):
            if dfs(crs) is False:
                return False
        return True