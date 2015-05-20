class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return [""]
        self.digits= ["","","abc","def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.ans,tmp = [],[]
        self.helper(digits,0,tmp)
        return self.ans


    def helper(self,digits,p,tmp):
        if p == len(digits):
            self.ans.append("".join(tmp))
            return
        for i in self.digits[ord(digits[p]) - ord('0')]:
            tmp.append(i)
            self.helper(digits,p+1,tmp)
            tmp.pop()


s = Solution()
print s.letterCombinations("2")