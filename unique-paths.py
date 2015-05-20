# @return an integer
def uniquePaths(m, n):
    dp = [[0 for i in range(n) ]for j in range(m)]
    if m == 0 and n == 0:
        return 0
    if m == 1 or n == 1:
        return 1
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            print str(i)+" "+str(j)
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]


print uniquePaths(3,7)