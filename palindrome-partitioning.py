class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s or len(s) == 0:
            return []
        item,res = [],[]
        self.helper(s,0,item,res)
        return res

    def ispalindrome(self,s):
        low,high = 0, len(s)-1
        while low < high:
            if s[low] != s[high]:
                return False
            low,high = low+1,high-1
        return True

    def helper(self,s,start,item,res):
        if start == len(s):
            res.append(item[:])
            return
        for i in range(start,len(s)):
            st = s[start:i+1]
            print st
            if self.ispalindrome(st):
                item.append(st)
                self.helper(s,i+1,item,res)
                item.pop()


s = Solution()
print s.partition("aabb")