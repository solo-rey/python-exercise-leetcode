# @param num, a list of integer
# @return a list of integer
def nextPermutation(num):
    """http://fisherlei.blogspot.com/2012/12/leetcode-next-permutation.html"""
    """need to remember the algo for permutation"""
    if not num or len(num) == 0:
        return
    p = False
    pos = -1
    for i in reversed(range(len(num)-1)):
        if num[i] < num[i+1]:
            pos = i
            p = True
            break
    if not p:
        return num[::-1]
    else:
        q = -1
        for i in reversed(range(len(num))):
            if i > pos and num[i] > num[pos]:
                q = i
                break
        num[pos],num[q] = num[q],num[pos]
        return num[:pos+1]+num[:pos:-1]


