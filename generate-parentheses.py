class Solution:
    # @param an integer
    # @return a list of string
    def helper(self,res,item,left,right):
        if left > right:
            return
        if left == 0 and right == 0:
            res.append(item)
            return
        if left > 0:
            self.helper(res,item+'(',left-1,right)
        if right > 0:
            self.helper(res,item+')',left,right-1)



    # @param an integer
    # @return a list of string
    def generateParenthesis(self,n):
        res = []
        item = ""
        if n <= 0:
            return res
        self.helper(res,item,n,n)
        return res
