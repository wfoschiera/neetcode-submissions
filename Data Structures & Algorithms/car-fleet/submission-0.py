class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target = 10
        # position = [4,1]
        # speed = [2,3]

        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        ord_cars = sorted(cars,key=lambda x: x[0], reverse=True)
        times = [(target - pos) / spd for pos, spd in ord_cars]
        fleets = 1
        for i in range(len(cars)-1):
            if times[i] >= times[i+1]:
                continue
            fleets += 1
        return fleets