from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_map = defaultdict(list)
        for crs, pre in prerequisites:
            adj_map[crs].append(pre)

        visited = set()
        scanned = set()

        def dfs(crs):
            if crs in visited:
                return False

            if adj_map[crs] == [] or crs in scanned:
                return True
            
            visited.add(crs)
            for pre in adj_map[crs]:
                if dfs(pre) is False:
                    return False
            scanned.add(crs)
            visited.remove(crs)
            return True

        for crs, _ in prerequisites:
            if dfs(crs) is False:
                return False
        return True