class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        maxInt = 0
        for i in range(len(s)):
            tmp = set()
            for j in range(i,len(s)):
                if s[j] not in tmp:
                    tmp.add(s[j])
                else:
                    if len(tmp) > maxInt:
                        maxInt = len(tmp)
            if maxInt == len(s):
                break
        return maxInt


import string


# @return an integer
def lengthOfLongestSubstring(s):
    """no assumation now"""
    """http://blog.csdn.net/likecool21/article/details/10858799"""
    if len(s) == 0:
        return 0
    maxv = 1
    start = 0
    dic = {}
    for i in range(len(string.printable)):
        dic[string.printable[i]] = -1
    dic[s[0]] = 0
    for idx in range(1,len(s)):
        if dic[s[idx]] >= start:
            start = dic[s[idx]]+1
        maxv = max(maxv,idx-start+1)
        dic[s[idx]] = idx
    return maxv

print lengthOfLongestSubstring("abcabcbb")