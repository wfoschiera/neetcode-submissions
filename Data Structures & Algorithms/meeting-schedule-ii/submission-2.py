"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        arr_s, arr_e = [], []
        for i in intervals:
            arr_s.append(i.start)
            arr_e.append(i.end)
        arr_s.sort()
        arr_e.sort()

        s = e = c = max_count = 0
        while s < len(arr_s):
            if arr_s[s] < arr_e[e]:
                c += 1
                max_count = max(c, max_count)
                s += 1
            else:
                c -= 1
                e += 1

        return max_count            