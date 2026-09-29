"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals=sorted(intervals,key=lambda x:x.start)
        i=0
        for j in range(1,len(intervals)):
            if intervals[i].end>intervals[j].start:
                return False
            i=j
        return True
