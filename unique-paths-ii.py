# @param obstacleGrid, a list of lists of integers
# @return an integer
def uniquePathsWithObstacles(obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        if m == 0 or n == 0:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        dp[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]

        for i in range(1,n):
                if obstacleGrid[0][i] == 1:
                    dp[0][i] = 0
                else:
                    dp[0][i] = dp[0][i-1]

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

