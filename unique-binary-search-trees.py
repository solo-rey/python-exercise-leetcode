class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 0 or n == 1:
            return 1
        c = [0 for i in range(n+1)]
        c[0] =1
        for num in range(1,n+1):
            for i in range(0,num):
                c[num]+=c[i]*c[(num-1)-i]
        return c[n]
