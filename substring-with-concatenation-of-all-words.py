# @param S, a string
# @param L, a list of string
# @return a list of integer
"""
Initially miss this line
                            if curdict[temp] < dict[temp]:
                                cnt-=1
"""
def findSubstring_steal(S, L):
    res = []
    if not S or not L or len(L) == 0:
        return res
    dict = {}
    for word in L:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word]+=1
    wordlen = len(L[0])
    for i in range(wordlen):
        cnt = 0
        index = i
        curdict = {}
        for j in range(i,len(S)-wordlen+1,wordlen):
            curword = S[j:j+wordlen]
            if curword not in dict:
                curdict.clear()
                cnt = 0
                index = j + wordlen
            else:
                if curword not in curdict:
                    curdict[curword] = 1
                else:
                    curdict[curword] +=1
                if curdict[curword] <= dict[curword]:
                    cnt+=1
                else:
                    while curdict[curword] > dict[curword]:
                        temp = S[index:index+wordlen]
                        if temp in curdict:
                            curdict[temp]-=1
                            if curdict[temp] < dict[temp]:
                                cnt-=1
                        index+=wordlen
                if cnt == len(L):
                    res.append(index)
                    temp = S[index:index+wordlen]

                    curdict[temp]-=1
                    cnt-=1
                    index+=wordlen
    return res

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        lenS,lenL,lenWord = len(S),len(L),len(L[0])
        res = []
        for i in range(lenS-lenL*lenWord+1):
            listS = [S[j:j+lenWord] for j in range(i,i+lenL*lenWord,lenWord)]
            flag = True
            for item in L:
                if item in listS:
                    listS.remove(item)
                else:
                    flag = False
                    break
            if flag:
                res.append(i)
        return res





