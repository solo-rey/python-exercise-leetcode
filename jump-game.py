class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        maxv = A[0]
        i = 1
        while i <= maxv and maxv < len(A)-1:
            maxv = max(maxv,A[i]+i)
            i+=1
        return maxv >= len(A)-1


s = Solution()
print s.canJump([2,3,1,1,4])
print s.canJump([3,2,1,0,4])