class Solution:
    # @return a string
    def countAndSay(self, n):
        if n <= 0:
            return ""
        start = 1
        cur = "1"
        while start < n:
            count=1
            st=""
            for i in range(1,len(cur)):
                if cur[i] == cur[i-1]:
                    count+=1
                else:
                    st+=str(count)
                    st+=cur[i-1]
                    count = 1
            st+=str(count)
            st+=cur[-1]
            cur = st
            start+=1
        return cur

s = Solution()
print s.countAndSay(4)


