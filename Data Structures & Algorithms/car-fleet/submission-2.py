class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        ord_cars = sorted(cars,key=lambda x: x[0], reverse=True)
        arrival_times = [(target - pos) / spd for pos, spd in ord_cars]
        fleets = 0
        prev_time = 0
        for curr_time in arrival_times:
            if curr_time > prev_time:
                fleets += 1
                prev_time = curr_time
        
        return fleets