class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices is None or len(prices) == 0:
            return 0
        arrayA=[0 for i in range(len(prices))]
        arrayB=[0 for i in range(len(prices))]
        minprice = prices[0]
        for i in range(1,len(prices)):
            minprice = min(minprice,prices[i])
            arrayA[i] = max(arrayA[i],prices[i]-minprice)
        maxprice=prices[-1]
        for i in reversed(range(len(prices)-1)):
            maxprice = max(maxprice,prices[i])
            arrayB[i] = max(arrayB[i+1],maxprice-prices[i])
        maxprofit=0
        for i in range(len(prices)):
            maxprofit=max(maxprofit,arrayA[i]+arrayB[i])
        return maxprofit