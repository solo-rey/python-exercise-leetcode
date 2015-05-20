class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if not s or len(s) == 0:
            return 0
        stk = []
        p = [0 for i in range(len(s))]
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                if len(stk) > 0:
                    p[i] = i - stk[-1] + 1
                    if i > p[i] and p[i-p[i]]:
                        p[i] += p[i-p[i]]
                    ans = max(ans,p[i])
                    stk.pop()
        return ans
