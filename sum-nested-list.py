def sumnestedlist(lst):
    """
     Question1 /** * Given a nested list of integers, returns
     the sum of all integers in the list weighted by their depth *
     For example, given the list {{1,1},2,{1,1}} the function should return 10 (four 1's at depth 2, one 2 at depth 1) * Given the list {1,{4,{6}}} the function should return 27
    (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3)
    """
    if lst is None or len(lst) == 0:
        return 0
    summ=0
    depth=1
    return helper(lst,depth,summ)


def helper(lst,depth,summ):
    if lst is None or len(lst) == 0:
        return summ
    for i in range(len(lst)):
        if isinstance(lst[i],list):
            summ+=helper(lst[i],depth+1,0)
        else:
            summ+=lst[i]*depth
    return summ

a=[[1,1],2,[1,1]]
print sumnestedlist(a)