class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        """

        ???????dp[i][j]????s1??i??s2??j???????s3??i+j??
        """
        if len(s3) != len(s1)+len(s2):
            return False
        dp = [[False] * (len(s2)+1) for i in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0  and j == 0:
                    dp[i][j] = True
                elif i > 0 and dp[i-1][j] and s3[i+j-1] == s1[i-1]:
                    dp[i][j] = True
                elif j > 0 and dp[i][j-1] and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[len(s1)][len(s2)]


s = Solution()
print s.isInterleave("a","","a")



