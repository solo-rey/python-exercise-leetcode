"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):



    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) <= 1:
            return True
        intervals = sorted(intervals, key=lambda x: x.start)
        end = intervals[0].end
        for i in range(1, len(intervals)):
            t = intervals[i]
            if t.start < end:
                return False
            elif end < t.end:
                end = t.end
        return True





c = Solution()
t = []
t.append(Interval(15,20))
t.append(Interval(5,10))
t.append(Interval(0,30))

print c.canAttendMeetings(t)