class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if not points or len(points) == 0:
            return 0
        allmax=0
        for i in range(len(points)):
            dic = {}
            localmax = 1 #local one node
            samenode = 0
            slope = 0.0
            for j in range(i+1,len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    samenode+=1
                    continue
                if points[i].x == points[j].x:
                    slope= 2147483647 #sys.maxint
                elif points[i].y == points[j].y:
                    slope = 0.0
                else:
                    slope = float(points[i].y - points[j].y) / float (points[i].x - points[j].x)
                if slope in dic:
                    dic[slope]+=1
                else:
                    dic[slope]=2
            for local in dic.values():
                localmax = max(localmax,local)
            localmax+=samenode
            allmax=max(allmax,localmax)
        return allmax
