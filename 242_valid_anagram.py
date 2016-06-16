"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if s == None or t == None:
            return False
        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = 1
            else:
                m[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in m:
                return False
            else:
                if m[t[i]] - 1 < 0:
                    return False
                m[t[i]] -= 1
        return True
