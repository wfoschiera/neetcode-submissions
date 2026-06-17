import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._nums = nums
        heapq.heapify(self._nums)

    def add(self, val: int) -> int:
        heapq.heappush(self._nums, val)
        nth = heapq.nlargest(self._k, self._nums)
        return nth[-1]