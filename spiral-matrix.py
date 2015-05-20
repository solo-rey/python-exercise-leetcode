class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == []:
            return []
        res = []
        maxUp = maxLeft = 0
        maxDown = len(matrix)-1
        maxRight = len(matrix[0])-1
        direct = 0
        while True:
            if direct==0:
                for i in range(maxLeft,maxRight+1):
                    res.append(matrix[maxUp][i])
                maxUp+=1
            elif direct == 1:
                for i in range(maxUp,maxDown+1):
                    res.append(matrix[i][maxRight])
                maxRight-=1
            elif direct == 2:
                for i in reversed(range(maxLeft,maxRight+1)):
                    res.append(matrix[maxDown][i])
                maxDown-=1
            else:
                for i in reversed(range(maxUp,maxDown+1)):
                    res.append(matrix[i][maxLeft])
            if maxUp > maxDown or maxLeft > maxRight:
                return res
            direct = (direct+1)%4
