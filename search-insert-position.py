class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        l,h = 0, len(A)
        while l < h:
            m = (l+h) // 2
            if A[m] < target:
                l = m+1
            else:
                h=m
        return l
