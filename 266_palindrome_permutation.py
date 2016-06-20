"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

Hint:

Consider the palindromes of odd vs even length. What difference do you notice?
Count the frequency of each character.
If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {}
        cnt = 0
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = 1
            else:
                m[s[i]] = m[s[i]] + 1
            cnt += 1
        if cnt % 2 == 0:
            for k,v in m.iteritems():
                if v % 2 != 0:
                    return False
            return True
        else:
            t = 0
            for k,v in m.iteritems():
                if v % 2 != 0:
                    t+=1
            return t <= 1