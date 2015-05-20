class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if not S or len(S) == 0:
            return S
        res,item = [],[]
        S.sort()
        for i in range(1,len(S)+1):
            self.helper(S,i,0,item,res)
        res.append([])
        return res


    def helper(self,S,n,start,item,res):
        if len(item) == n:
            #print item
            res.append(item[:])
            return
        for i in range(start,len(S)):
           # print S
            item.append(S[i])
            self.helper(S,n,i+1,item,res)
            item.pop()


s = Solution()
print s.subsets([1,2,3])