class Solution:
    """
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        fn_1 = 1
        fn_2 = 2
        fn = 0
        if n == 1:
            return fn_1
        if n == 2:
            return fn_2
        for i in range(3,n+1):
            fn = fn_1 + fn_2
            fn_1 = fn_2
            fn_2 = fn
        return fn

# @param n, an integer
# @return an integer
def climbStairs(n):
    dp = [0 for i in range(n+1)]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n-1]