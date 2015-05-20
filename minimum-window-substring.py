# @return a string
def minWindow_steal(S, T):
    if not S or len(S) == 0:
        return ""
    dic = {}
    for char in T:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char]+=1
    minLen = len(S)+1
    left = 0
    cnt = 0
    minStart = 0
    for idx in range(len(S)):
        if S[idx] in dic:
            print "haha "+str(idx)+" "+str(minLen)+" "+str(cnt)
            dic[S[idx]]-=1 #for duplication char check
            if dic[S[idx]] >= 0:
                cnt+=1
            while cnt == len(T):
                print str(cnt)+" "+str(idx)+" "+str(left)
                if idx-left+1 < minLen:
                    minLen = idx-left+1
                    minStart=left
                    if minLen == len(T):
                        return S[minStart:minStart+minLen]
                if S[left] in dic:
                    dic[S[left]]+=1
                    if dic[S[left]] >0:
                        cnt-=1
                left+=1
    if minLen > len(S):
        return ""
    return S[minStart:minStart+minLen]





def minWindow(S,T):
    if not S or len(S) == 0:
        return ""
    dic = {}
    for char in T:
        if char not in dic:
            dic[char]=1
        else:
            dic[char]+=1

    minLen = len(S)+1
    minStart = 0
    left = 0
    cnt = 0
    for idx in range(len(S)):
        if S[idx] in dic:
            dic[S[idx]]-=1 #remove duplication to correct count cnt: e.g "bba","ab"
            if dic[S[idx]] >= 0:
                cnt+=1
            while cnt == len(T):
                if idx-left+1 < minLen:
                    minLen = idx-left+1
                    minStart=left
                    if minLen == len(T):
                        return S[minStart:minStart+minLen]
                if S[left] in dic:
                    dic[S[left]]+=1
                    if dic[S[left]] > 0:
                        cnt-=1
                left+=1
    if minLen > len(S):
        return ""
    return S[minStart:minStart+minLen]





#print minWindow("ADOBECODEBANC","ABC")
print minWindow_steal("bbbbbbbbbb","bb")