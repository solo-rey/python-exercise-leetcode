class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        maxprofit = 0
        for i in range(1,len(prices)):
            delta = prices[i] - prices[i-1]
            if delta > 0:
                maxprofit+=delta
        return maxprofit