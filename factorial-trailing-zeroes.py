class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        cnt = 0
        i = 5
        while n/i >= 1:
            cnt += n/i
            i*=5
        return cnt