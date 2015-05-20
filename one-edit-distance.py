class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):
        if s == "" and t == "":
            return False
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) > len(t):
            return self.isOneEditDistance(t,s)
        i = 0
        shift = len(t) - len(s)
        while i < len(s) and s[i] == t[i]:
            i+=1
        if i == len(s):
            return shift > 0
        if shift == 0:
            i+=1
        while i < len(s) and s[i] == t[i+shift]:
            i+=1
        return i==len(s)