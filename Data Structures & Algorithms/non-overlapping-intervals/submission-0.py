class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        i, j = 0, 1
        prev_end = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            if start < prev_end:
                count += 1
                prev_end = min(prev_end, end)
                j += 1
            else:
                prev_end = end
        return count