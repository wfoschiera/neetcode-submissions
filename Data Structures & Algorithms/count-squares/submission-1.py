class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points[point] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        total = 0
        valid_diagonals = []
        for p in self.points:
            x2,y2 = p
            delta_x = abs(x1-x2)
            delta_y = abs(y1-y2)
            if delta_x > 0 and delta_y > 0 and delta_x == delta_y:
                valid_diagonals.append(p)
        
        for diag in valid_diagonals:
            c1 = tuple([x1, diag[1]])
            c2 = tuple([diag[0], y1])
            if c1 in self.points and c2 in self.points:
                total += self.points[diag] * self.points.get(c1) * self.points.get(c2)
        return total