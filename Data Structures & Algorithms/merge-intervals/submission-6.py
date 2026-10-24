class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        i, j = 0, 1
        while j <= len(intervals) - 1:
            x1, y1 = intervals[i]
            x2, y2 = intervals[j]
            # overlap
            if y1 >= x2:
                intervals[i] = [min(x1, x2), max(y1, y2)]
                j +=1
            else:
                i +=1
                intervals[i] = [x2, y2]
                j +=1
            
        for _ in range(len(intervals)-1 - i):
            intervals.pop()
        return intervals
