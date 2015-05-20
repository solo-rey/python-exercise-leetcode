class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.cnt=0
        loc=[-1 for i in range(n)]
        self.helper(loc,0,n)
        return self.cnt



    def helper(self,loc,cur,n):
        if cur == n:
            self.cnt+=1
        else:
            for i in range(n):
                loc[cur] = i
                if self.isValid(loc,cur):
                    self.helper(loc,cur+1,n)



    def isValid(self,loc,cur):
        for i in range(cur):
            if loc[i] == loc[cur] or abs(loc[i] - loc[cur]) == cur - i:
                return False
        return True


s = Solution()
print s.totalNQueens(1)