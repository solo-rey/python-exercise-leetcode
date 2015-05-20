class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        i,j,star,mark = 0,0,-1,-1
        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i+=1
                j+=1
            elif j < len(p) and p[j] == '*':
                j+=1
                star=j
                mark=i
            elif star != -1:
                j=star
                i=mark+1
                mark+=1
            else:
                return False
        while j < len(p) and p[j] == '*':
            j+=1
        return j==len(p)

