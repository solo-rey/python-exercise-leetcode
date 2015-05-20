class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

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

