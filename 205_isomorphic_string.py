"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and t or s and not t:
            return False
        if len(s) != len(t):
            return False
        comp_map = {}
        for i in range(len(s)):
            if s[i] not in comp_map:
                comp_map[s[i]] = t[i]
            else:
                if t[i] != comp_map[s[i]]:
                    return False
        another_map = {}
        for i in range(len(t)):
            if t[i] not in another_map:
                another_map[t[i]] = s[i]
            else:
                if s[i] != another_map[t[i]]:
                    return False
        return True


s =Solution()
print s.isIsomorphic("egg", "add")
print s.isIsomorphic("foo", "bar")
print s.isIsomorphic("paper", "title")
print s.isIsomorphic("ab","aa")