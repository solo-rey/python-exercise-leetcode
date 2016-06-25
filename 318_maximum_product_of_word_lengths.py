"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        masks = []
        res = 0
        for i in range(len(words)):
            c_lst = list(words[i])
            j = 0
            for k in range(len(c_lst)):
                j |= 1 << (ord(c_lst[k]) - ord('a'))
            masks.append(j)
            for j in range(i):
                if masks[j] & masks[i] == 0:
                    res = max(res, len(words[j]) * len(words[i]))
        return res



c = Solution()
print c.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
