class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        ord_cars = sorted(cars,key=lambda x: x[0], reverse=True)
        arrival_times = [(target - pos) / spd for pos, spd in ord_cars]
        fleets = 0
        slowest = 0
        for t in arrival_times:
            if t > slowest:
                fleets += 1
                slowest = t
        
        return fleets