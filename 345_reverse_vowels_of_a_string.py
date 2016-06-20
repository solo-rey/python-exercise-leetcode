"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
"""

class Solution(object):
    @staticmethod
    def isVowel(c):
        if c == 'a' or c == 'A' \
            or c == 'e' or c == 'E' \
            or c == 'i' or c == 'I' \
            or c == 'o' or c == 'O' \
            or c == 'u' or c == 'U':
            return True
        return False
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s)-1
        while left < right:
            if self.isVowel(s[left]) and self.isVowel(s[right]):
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1
            elif self.isVowel(s[left]):
                right-=1
            else:
                left+=1
        return s