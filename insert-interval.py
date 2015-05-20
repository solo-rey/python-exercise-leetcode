# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
    def __str__(self):
        return str(self.start)+" "+str(self.end)

# @param intervals, a list of Intervals
# @param newInterval, a Interval
# @return a list of Interval
def insert_notworking(intervals, newInterval):
    lst = list(intervals)
    startidx = -999
    for idx in range(len(intervals)):
        if newInterval.end < intervals[idx].start:
            if startidx == -999:
                lst.insert(0,newInterval)
            else:
                print startidx
                lst.insert(startidx,newInterval)
            return lst
        elif newInterval.start > intervals[idx].end:
            startidx = idx
            continue
        else:
            if startidx == -999:
                startidx = idx
            newInterval.start = min(newInterval.start,intervals[idx].start)
            newInterval.end = max(newInterval.end,intervals[idx].end)
            lst.remove(intervals[idx])
    if startidx == -999:
        lst.append(newInterval)
    else:
        lst.insert(startidx+1,newInterval)
    return lst

def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort(key=lambda x:x.start)
    res = [intervals[0]]
    for i in range(1,len(intervals)):
        if res[-1].start <= intervals[i].start <= res[-1].end:
            res[-1].end = max(intervals[i].end,res[-1].end)
        else:
            res.append(intervals[i])
    return res
