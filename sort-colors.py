# @param A a list of integers
# @return nothing, sort in place
def sortColors_twopass(A):
    one=0
    two=0
    zero=0
    for i in range(len(A)):
        if A[i] == 0:
            zero+=1
        elif A[i] == 1:
            one+=1
        elif A[i] == 2:
            two+=1
    for i in range(0,zero):
        A[i] = 0
    if one != 0:
        for i in range(zero,one+zero):
            A[i] = 1
    if one != 0:
        for i in range(one+zero,one+zero+two):
            A[i] = 2
    else:
        for i in range(zero,zero+two):
            A[i] = 2
    print A


def sortColors_onepass(A):
    if not A or len(A) == 0:
        return
    red = 0
    blue = len(A)-1
    i = 0
    while i < blue+1:
        if A[i] == 0:
            A[red],A[i] = A[i],A[red]
            red+=1
            i+=1
            continue
        if A[i] == 2:
            A[blue],A[i] = A[i],A[blue]
            blue-=1
            continue
        i+=1
    print A




sortColors_twopass([1,2,0])

sortColors_onepass([1,0])
