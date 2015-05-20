class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for i in range(len(word2)+1):
            dp[0][i] = i
        for i in range(1,len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    #dp[i][j]: #compare word1 first i char and word2 first j char, how many steps for convert
                    #dp[i-1][j-1]+1: #swap the char in word1 position i with word2 position j
                    #dp[i-1][j]+1: #delete the char in word1 in position i
                    #dp[i][j-1]+1 #insert the char in word2 posistion j to word1 posistion i
                    dp[i][j] = min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[len(word1)][len(word2)]
