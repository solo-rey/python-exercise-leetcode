class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum_old(self, num):
        if not num or len(num) == 0:
            return []
        res = []
        num.sort()
        for i in range(len(num)-2):
            if i==0 or num[i]!=num[i-1]:
                low=i+1
                high=len(num)-1
                while low < high:
                    tmpsum=num[i]+num[low]+num[high]
                    if tmpsum==0:
                        tmphs=[]
                        tmphs.append(num[i])
                        tmphs.append(num[low])
                        tmphs.append(num[high])
                        if tmphs not in res:
                            res.append(tmphs)
                        low+=1
                        high-=1
                    elif tmpsum>0:
                        high-=1
                    else:
                        low+=1
        return res

    def threeSum(self,num):
        if not num or len(num) < 3:
            return []
        num.sort()
        res=[]
        for i in range(len(num)):
            if i == 0 or num[i] != num[i-1]:
                l,r=i+1,len(num)-1
                while l<r:
                    tmpsum=num[i]+num[l]+num[r]
                    if tmpsum==0:
                        res.append([num[i],num[l],num[r]])
                        while l < r and num[l] == num[l+1]:
                            l+=1
                        while l<r and num[r] == num[r-1]:
                            r-=1
                        l,r=l+1,r-1
                    elif tmpsum<0:
                        l+=1
                    elif tmpsum>0:
                        r-=1
        return res



s = Solution()
print (s.threeSum([0,0,0]))

