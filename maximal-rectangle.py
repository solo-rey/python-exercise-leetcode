class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maxArea = 0
        height = [0 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    height[j] = 0
                else:
                    height[j]+=1
            maxArea = max(maxArea,self.largestRectangleArea(height))
        return maxArea



    def largestRectangleArea_TLE(self,height):
        #this will TLE,needs to use stack version
        minh = [0 for i in range(len(height))]
        maxarea = 0
        for i in range(len(height)):
            if height[i] != 0 and maxarea/height[i] >= (len(height) - i):
                continue
            for j in range(i,len(height)):
                if i == j:
                    minh[j] = height[j]
                else:
                    if height[j] < minh[j-1]:
                        minh[j] = height[j]
                    else:
                        minh[j] = minh[j-1]
                localarea = minh[j]*(j-i+1)
                maxarea = max(maxarea,localarea)
        return maxarea

    def largestRectangleArea(self, height):
        maxsize,lenh,stk = 0,len(height),[]
        for i in range(lenh+1):
            while len(stk) and (i == lenh or height[stk[-1]] >= height[i]):
                top = stk.pop()
                if len(stk) == 0:
                    maxsize = max(maxsize,height[top]*i)
                else:
                    maxsize = max(maxsize,height[top]*(i-stk[-1]-1))
            stk.append(i)
        return maxsize