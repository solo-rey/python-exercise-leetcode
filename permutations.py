class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if not num or len(num) == 0:
            return []
        used = [False for i in range(len(num))]
        res = []
        self.permutehelper(num,used,[],res)
        return res


    def permutehelper(self,num,used,item,res):
        if len(item) == len(num):
            res.append(item[:])
        for i in range(len(num)):
            if not used[i]:
                used[i]= True
                item.append(num[i])
                self.permutehelper(num,used,item,res)
                used[i] = False
                item.pop()
        return res

    def permute_iterative(self,nums):
        solutions = [[]]
        for num in nums:
            next = []
            for solution in solutions:
                print solution
                for i in range(len(solution) + 1):
                    next.append(solution[:i] + [num] + solution[i:])
            solutions = next
        return solutions


s = Solution()
print s.permute_iterative([1])

