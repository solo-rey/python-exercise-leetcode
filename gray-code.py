class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0: return [0]
        L = [0, 1]
        for i in xrange(2, n + 1):
            t = 1 << (i - 1)
            L = L + [ j + t for j in L[::-1] ]
        return L