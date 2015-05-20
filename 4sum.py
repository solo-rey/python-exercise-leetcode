class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if num is None or len(num) < 4:
            return []
        res = []
        num.sort()
        for i in range(len(num)):
            if i == 0 or num[i] != num[i-1]:
                for j in range(i+1,len(num)):
                    if num[j] != nump[j-1]:
                        l,r=j+1,len(num)-1
                        while l < r:
                            tmpsum = num[i]+num[j]+num[l]+num[r]
                            if tmpsum == target:
                                res.append([num[i],num[j],num[l],num[r]])
                                while l<r and num[l]==num[l+1]:
                                    l+=1
                                while l<r and num[r]==num[r-1]:
                                    r-=1
                                l,r=l+1,r-1
                            elif tmpsum<target:
                                l+=1
                            elif tmpsum>target:
                                r-=1
        return res