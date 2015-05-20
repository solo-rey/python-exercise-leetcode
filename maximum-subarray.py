# @param A, a list of integers
# @return an integer
def maxSubArray(A):
    maxv = -9999
    sumv = 0
    for i in A:
        sumv += i
        maxv = max(maxv,sumv)
        if sumv < 0:
            sumv=0
    return maxv