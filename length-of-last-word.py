class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        st = s.split()
        if len(st) == 0:
            return 0
        return len(st[-1])
