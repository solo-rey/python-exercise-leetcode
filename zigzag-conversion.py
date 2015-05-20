class Solution:
    # @return a string
    def convert(self, s, nRows):
        if s is None or s == "" or nRows <= 0:
            return ""
        if nRows == 1:
            return s
        size = 2*nRows-2
        st=""
        for i in range(nRows):
            for j in range(i,len(s),size):
                st+=s[j]
                if i != 0 and i != nRows-1 and j+size-2*i < len(s):
                    st+=s[j+size-2*i]
        return st

s= Solution()
print s.convert("ABC",2)