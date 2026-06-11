from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # one line solution O(nlogn)
        # sorted(points, key=lambda x: (x[0]**2 + x[1]**2)**(1/2))[:k]

        return sorted(points, key=lambda x: (x[0]**2 + x[1]**2)**(1/2))[:k]
