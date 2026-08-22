class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_map = []
        for point in points:
            x, y = point
            distance = (x + y)
            if len(distance_map) == 0:
                distance_map.append((point, distance))
            else:
                l = 0
                r = len(distance_map)
                while l < r:
                    mid = l + ((r - l) // 2)
                    if distance > distance_map[mid][1]:
                        l = mid
                    elif distance < distance_map[l][1]:
                        r = mid
                distance_map = distance_map[0:l] + [(point, distance)] + distance_map[l:]

        result = distance_map[0:k]
        return [point for point, distance in result]
