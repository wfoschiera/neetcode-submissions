class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def search(intervals, target):
            start = 0
            end = len(intervals) - 1
            while start <= end:
                mid = (end + start) // 2
                if intervals[mid][0] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return start 
            
        def is_overlap(i1, i2):
            return max(i1[0], i2[0]) <= min(i1[1], i2[1])
        
        def merge(i1, i2):
            start = min(i1[0], i2[0])
            end = max(i1[1], i2[1])
            return [start, end] 

        idx = search(intervals, newInterval[0])
        intervals.insert(idx, newInterval)
        
        res = []
        for interval in intervals:
            if not res or not is_overlap(res[-1], interval):
                res.append(interval)
            else:
                res[-1] = merge(res[-1], interval)
        return res