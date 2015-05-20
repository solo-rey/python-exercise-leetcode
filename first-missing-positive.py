class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A or len(A) == 0:
            return 1
        for i in range(len(A)):
            while A[i] <= len(A) and A[i] > 0 and A[A[i] - 1] != A[i]:
                A[A[i] - 1],A[i] = A[i], A[A[i] -1]
        for i in range(len(A)):
            if A[i] != i+1:
                return i+1
        return len(A)+1


s = Solution()
print s.firstMissingPositive([3,4,-1,1])
