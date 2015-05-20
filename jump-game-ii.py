class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if not A or len(A) == 0:
            return 0
        maxcover,step,lastcover = 0,0,0
        i = 0
        while i <= maxcover and i <= len(A) - 1:

            if i > lastcover:
                step+=1
                lastcover = maxcover
            if A[i]+i > maxcover:
                maxcover=A[i]+i

            i+=1
        if maxcover < len(A)-1:
            return 0
        return step

s= Solution()
print s.jump([2,1])