class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if not s or len(s) <= 1:
            return s
        longest = s[0:1]
        for i in range(0,len(s)):
            tmp = self.helper(s,i,i)
            if len(tmp) > len(longest):
                longest = tmp
            tmp = self.helper(s,i,i+1)
            if len(tmp) > len(longest):
                longest = tmp
        return longest




    def helper(self,s,start,end):
        while start >= 0 and end <= len(s)-1 and s[start] == s[end]:
            start-=1
            end+=1
        return s[start+1:end]


s = Solution()
print s.longestPalindrome("ababdc")


def longestPalindrome(s):
    if not s or len(s) <= 1:
        return s
    longest = s[0:1]
    for i in range(0, len(s)):
        tmp_str = helper(s, i, i)
        if len(tmp_str) > len(longest):
            longest = tmp_str
        tmp_str = helper(s, i, i+1)
        if len(tmp_str) > len(longest):
            longest = tmp_str
    return longest


def helper(s, start, end):
    if start >= 0 and end <= len(s)-1 and s[start] == s[end]:
        start -= 1
        end += 1
    return s[start+1 : end]