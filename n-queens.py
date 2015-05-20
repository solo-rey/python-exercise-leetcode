class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        res = []
        loc = [-1 for i in range(n)]
        self.helper(res,loc,0,n)
        return res


    def helper(self,res,loc,cur,n):
        if cur == n:
            ans = []
            for i in range(n):
                st = ""
                for j in range(n):
                    if j == loc[i]:
                        st+='Q'
                    else:
                        st+='.'
                ans.append(st)
            res.append(ans)
        else:
            for i in range(n):
                loc[cur] = i
                if self.isValid(loc,cur):
                    self.helper(res,loc,cur+1,n)

    def isValid(self,loc,cur):
        for i in range(cur):
            if loc[i] == loc[cur] or abs(loc[i] - loc[cur]) == cur-i:
                return False
        return True


s = Solution()
print s.solveNQueens(6)