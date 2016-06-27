class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        new_list = []
        new_list.append(intervals[0])
        for i in range(1, len(intervals)):
            t = intervals[i]
            if t.start <= new_list[-1].end:
                new_list[-1].end = max(new_list[-1].end, t.end)
            else:
                new_list.append(t)
        return new_list


t = []
t.append(Interval(1,4))
t.append(Interval(0,2))
t.append(Interval(3,5))
c = Solution()
c.merge(t)




# @param intervals, a list of Interval
# @return a list of Interval
def merge(intervals):
    if len(intervals) == 0:
        return intervals
    intervals.sort(key=lambda x:x.start)
    res = [intervals[0]]
    for i in range(1,len(intervals)):
        if res[-1].start <= intervals[i].start <= res[-1].end:
            res[-1].end = max(res[-1].end,intervals[i].end)
        else:
            res.append(intervals[i])
    return res

