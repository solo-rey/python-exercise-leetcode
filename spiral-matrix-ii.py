class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0:
            return []
        maxLeft,maxUp = 0,0
        maxDown,maxRight=n-1,n-1
        res = [[0 for i in range(n)] for j in range(n)]
        cur=0
        direct = 0
        while True:
            if direct == 0:
                for i in range(maxLeft,maxRight+1):
                    cur+=1
                    res[maxUp][i] = cur
                maxUp+=1
            elif direct == 1:
                for i in range(maxUp,maxDown+1):
                    cur+=1
                    res[i][maxRight] = cur
                maxRight-=1
            elif direct == 2:
                for i in reversed(range(maxLeft,maxRight+1)):
                    cur+=1
                    res[maxDown][i] = cur
                maxDown-=1
            else:
                for i in reversed(range(maxUp,maxDown+1)):
                    cur+=1
                    res[i][maxLeft]=cur
                maxLeft+=1
            if cur >= n*n:
                return res
            direct = (direct+1)%4
