class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if n <= 0 or n < k:
            return []
        res,item = [],[]
        self.helper(n,k,1,item,res)
        return res

    def helper(self,n,k,start,item,res):
        if len(item) == k:
            print item
            res.append(item[:])
            return
        for i in range(start,n+1):
            print item
            item.append(i)
            self.helper(n,k,i+1,item,res)
            item.pop(-1)

s = Solution()
print s.combine(3,3)
