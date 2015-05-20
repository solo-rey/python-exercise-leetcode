class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if not num or len(num) <= 1:
            return num
        used = [False for i in range(len(num))]
        num.sort()
        return self.permuteHelper(used,num,[],[])


    def permuteHelper(self,used,num,item,res):
        print str(item)+" "+str(num)+" "+str(res)+" "+str(used)
        if len(item) == len(num):
            res.append(item[:])
            return res
        for i in range(len(num)):
            if i > 0 and not used[i-1] and num[i] == num[i-1]:
                continue
            if not used[i]:
                used[i] = True
                item.append(num[i])
                self.permuteHelper(used,num,item,res)
                used[i] = False
                item.pop()
        return res



s = Solution()
print s.permuteUnique([1,1])


