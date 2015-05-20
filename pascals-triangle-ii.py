class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        currow = [1]
        res = []
        res.append(currow)
        for i in range(1,rowIndex+1):
            prevrow = currow
            currow = [1]
            for i in range(i-1):
                currow.append(prevrow[i]+prevrow[i+1])
            currow.append(1)
            res.append(currow)
        return res[rowIndex]