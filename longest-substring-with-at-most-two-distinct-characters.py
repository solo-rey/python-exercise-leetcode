class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if s is None or s == "":
            return 0
        p1,p2,longest=-1,-1,0
        start = 0
        for i in range(len(s)):
            if p1 == -1 or s[i] == s[p1]:
                p1 = i
            elif p2 == -1 or s[i] == s[p2]:
                p2 = i
            else:
                minl = min(p1,p2)
                start = minl+1
                if p1 == minl:
                    p1 = i
                else:
                    p2 = i
            longest = max(longest,i-start+1)
        return longest