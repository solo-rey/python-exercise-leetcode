class Solution:
    # @param height, a list of integer
    # @return an integer
    #O(N)
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


    def largestRectangleArea_n2(self,height):
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
