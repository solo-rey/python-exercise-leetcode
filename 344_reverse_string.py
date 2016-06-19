"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseString_normal(self, s):
        if len(s) <= 1:
            return s
        left, right = 0, len(s)-1
        while left < right:
            t = s[left]
            s[left] = s[right]
            s[right] = t
            left+=1
            right-=1
        return s


s = Solution()
print s.reverseString_normal("hellos")
