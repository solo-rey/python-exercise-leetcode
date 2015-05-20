# @param    A       a list of integers
# @param    elem    an integer, value need to be removed
#remove elements in place
# @return an integer
def removeElement(A, elem):
    if not A or len(A) == 0:
        return 0
    cur = 0
    for i in range(len(A)):
        if A[i] != elem:
            A[cur]=A[i]
            cur+=1
    return len(A[:cur])

print removeElement([2],3)
