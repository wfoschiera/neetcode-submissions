"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ordered = sorted(intervals, key=lambda x: x.start)
        for i in range(len(ordered) -1):
            if ordered[i].end > ordered[i+1].start:
                return False

        return True