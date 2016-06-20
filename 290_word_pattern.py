"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        str_lst = str.split()
        if len(pattern) != len(str_lst):
            return False
        map1 = {}
        for i in range(len(pattern)):
            map1[i] = pattern[i]
        map2 = {}
        map3 = {}
        for i in range(len(str_lst)):
            if map1[i] not in map2:
                map2[map1[i]] = str_lst[i]
            else:
                if map2[map1[i]] != str_lst[i]:
                    return False
            if str_lst[i] not in map3:
                map3[str_lst[i]] = map1[i]
            else:
                if map3[str_lst[i]] != map1[i]:
                    return False
        return True


s = Solution()
print s.wordPattern("abba", "dog cat cat dog")
print s.wordPattern("abba", "dog cat cat fish")
print s.wordPattern("aaaa", "dog cat cat dog")
print s.wordPattern("abba", "dog dog dog dog")

