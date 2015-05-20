class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if num is None or len(num) < 0:
            return
        num.sort()
        res=None
        for i in range(len(num)):
            l,r=i+1,len(num)-1
            while l<r:
                tmpsum=num[i]+num[l]+num[r]
                if res is None or abs(tmpsum-target) < abs(res-target):
                    res = tmpsum
                if tmpsum<=target:
                    l+=1
                elif tmpsum>=target:
                    r-=1
        return res


s = Solution()
print s.threeSumClosest([0,2,1,-3], 1)