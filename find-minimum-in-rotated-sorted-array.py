class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if num is None or len(num) == 0:
            return 0
        l,r=0,len(num)-1
        minnum = num[0]
        while l < r-1:
            m = (l+r)/2
            if num[l] < num[m]:
                minnum = min(minnum,num[l])
                l=m+1
            elif num[l] > num[m]:
                minnum = min(minnum,num[m])
                r=m-1
            else:
                l+=1

        minnum = min(minnum,num[l],num[r])
        return minnum


s = Solution()
print s.findMin([3,4,5,1,2])