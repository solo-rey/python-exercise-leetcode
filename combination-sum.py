class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        if not candidates or len(candidates) == 0:
            return []
        res,item = [],[]
        candidates.sort()
        self.helper(candidates,0,target,item,res)
        return res

    def helper(self,candidates,start,target,item,res):
        if target < 0 :
            return
        if target == 0:
            res.append(item[:])
            return
        for i in range(start,len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            item.append(candidates[i])
            self.helper(candidates,i,target-candidates[i],item,res)
            item.pop()
