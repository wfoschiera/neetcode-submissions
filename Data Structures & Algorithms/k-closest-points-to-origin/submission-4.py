from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance_map = defaultdict(list)
        # for point in points:
        #     x, y = point
        #     distance = (x + y)
        #     if len(distance_map) == 0:
        #         distance_map[(distance)].append(point)
        # distance_list = sorted(distance_map.values(), key=lambda x: x[0])
        # result = distance_list[0:k+1]

        return sorted(points, key=lambda x: (x[0]**2 + x[1]**2)**(1/2))[:k]
