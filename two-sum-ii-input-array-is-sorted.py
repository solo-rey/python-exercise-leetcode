class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if num is None:
            return None
        i,j=0,len(num)-1
        while i <= j:
            a,b = num[i],num[j]
            if a+b == target:
                return (i+1,j+1)
            elif a+b < target:
                i+=1
                continue
            elif a+b > target:
                j-=1
                continue
        return None