class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s or len(s) == 0:
            return True
        i,j = 0,len(s)-1
        while i < j:
            if s[i] not in string.ascii_letters and s[i] not in string.digits:
                i+=1
                continue
            if s[j] not in string.ascii_letters and s[j] not in string.digits:
                j-=1
                continue
            if s[i] in string.ascii_letters:
                h = string.lower(s[i])
            if s[j] in string.ascii_letters:
                t = string.lower(s[j])
            if h != t:
                return False
            i+=1
            j-=1
        return True

s = Solution()
print s.isPalindrome("ab")
