def reversedsumlist(lst):
    if lst is None or len(lst) == 0:
        return 0
    sumlevel=[]
    depth=1
    helper(lst,depth,sumlevel)
    summ=0
    depth=len(sumlevel)
    for i in range(len(sumlevel)):
        print str(depth)+" "+str(sumlevel[i])
        summ+=depth*sumlevel[i]
        depth-=1
    return summ



def helper(lst,depth,sumlevel):
    if lst is None or len(lst) == 0:
        return
    for i in range(len(lst)):
        if isinstance(lst[i],list):
            helper(lst[i],depth+1,sumlevel)
        else:
            if depth>=len(sumlevel):
                for j in range(len(sumlevel),depth):
                    sumlevel.append(0)
                sumlevel.append(lst[i])
            else:
                sumlevel[depth]+=lst[i]



a = [[1,1],2,[1,1]]
b=[[2],1,[4,[6]]]
c=[1,[4,[6]]]
print reversedsumlist(a)