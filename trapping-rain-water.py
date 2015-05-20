# @param A, a list of integers
# @return an integer
def trap(A):
    if not A or len(A) == 0:
        return 0
    left = {}
    right = {}
    maxv = A[0]
    for i in range(1,len(A)):
        left[i] = max(maxv,A[i])
        maxv = max(maxv,A[i])
    maxv = A[-1]
    for i in reversed(range(len(A)-1)):
        right[i] = max(maxv,A[i])
        maxv = max(maxv,A[i])
    total = 0
    for i in range(1,len(A)-1):
        tmp = min(left[i],right[i])-A[i]
        if tmp > 0:
            total+=tmp
    return total

