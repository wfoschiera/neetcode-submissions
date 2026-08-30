import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = [] # stores larger half
        self.max_heap = [] # stores smaller half (negated for min-heap implementation)

    def addNum(self, num: int) -> None:
        # using python 3.14
        # From the docs
        # Push item on the max-heap heap, then pop and return the largest 
        # item from heap. The combined action runs more efficiently than
        # heappush_max() followed by a separate call to heappop_max().

        # push to heap_max and pop the higher value
        mean_val = heapq.heappushpop_max(self.max_heap, num)
        # push the mean value to heap_min 
        heapq.heappush(self.min_heap, mean_val)
        if len(self.min_heap) > len(self.max_heap):
            # keep both heaps balanced
            heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + self.max_heap[0]) / 2.0
        return float(self.max_heap[0])