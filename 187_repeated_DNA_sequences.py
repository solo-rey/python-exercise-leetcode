"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) <= 10:
            return []
        s_lst = []
        s_map = {}
        for i in range(len(s)-9):
            tmp = s[i:i+10]
            if tmp not in s_map:
                s_map[tmp] = 1
            else:
                if tmp not in s_lst:
                    s_lst.append(tmp)
                s_map[tmp] = s_map[tmp] + 1
        return s_lst

s = Solution()
# print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print s.findRepeatedDnaSequences("AAAAAAAAAAA")