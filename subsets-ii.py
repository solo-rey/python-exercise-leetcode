class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        res = []
        self.helper(S,0,0,res,[])
        return res

    def helper(self,S,depth,start,res,valuelist):
        if valuelist not in res:
            print valuelist
            res.append(valuelist)
        if depth == len(S):
            return
        for i in range(start,len(S)):
            self.helper(S,depth+1,i+1,res,valuelist+[S[i]])



s = Solution()
print s.subsetsWithDup([1,2,3,0])