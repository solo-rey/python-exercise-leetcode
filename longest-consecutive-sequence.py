class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        """
        take-away: use hash-map to record, and del all the one that is list contiguously
        """
        if not num:
            return 0
        longest = 1
        dic = {}
        for i in num:
            if i not in dic:
                dic[i] = 1
        for i in num:
            if i not in dic:
                continue
            length = 1
            while i-1 in dic:
                i-=1
            del dic[i]
            while i+1 in dic:
                i+=1
                length+=1
                del dic[i]
            longest = max(longest,length)
        return longest

    def longestConsecutive1(self, num):
        if not num:
            return 0
        dic = {}
        for i in num:
            if i not in dic:
                dic[i] = 1
        longest = 1
        for i in num:
            if i not in dic:
                continue
            length = 1
            while i-1 in dic:
                i-=1
            del dic[i]
            while i+1 in dic:
                length+=1
                i+=1
                del dic[i]
            longest = max(longest,length)
        return longest
