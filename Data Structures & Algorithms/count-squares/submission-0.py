class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points[point] += 1

    def count(self, point: List[int]) -> int:
        point = tuple(point)
        total = 0
        valid_diagonals = []
        for p in self.points:
            x1,y1 = p
            x2,y2 = point
            delta_x = abs(x1-x2)
            delta_y = abs(y1-y2)
            if delta_x > 0 and delta_y > 0 and delta_x == delta_y:
                valid_diagonals.append(p)
        x, y = point
        for (qx, qy) in valid_diagonals:
            c1 = tuple([x, qy])
            c2 = tuple([qx, y])
            if c1 in self.points and c2 in self.points:
                total += self.points[(qx, qy)] * self.points.get(c1) * self.points.get(c2)
        return total