class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        length = len(triangle)
        dp =[0 for i in range(length)]
        for i in triangle:
            oldDp = dp[:]
            for j in range(len(i)):
                if j == 0:
                    dp[j] = oldDp[j]+i[j]
                elif j == len(i)-1:
                    dp[j] = oldDp[j-1]+i[j]
                else:
                    dp[j] = min(oldDp[j],oldDp[j-1])+i[j]
        return min(dp)