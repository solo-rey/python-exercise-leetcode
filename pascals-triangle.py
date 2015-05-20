class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        currow = [1]
        res = []
        res.append(currow)
        for i in range(1,numRows):
            prevrow = currow
            currow = [1]
            for i in range(i-1):
                currow.append(prevrow[i]+prevrow[i+1])
            currow.append(1)
            res.append(currow)
        return res
