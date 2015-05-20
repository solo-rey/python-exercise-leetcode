# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    pass

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        if n==0:
            buf=""
            return 0
        readbytes=0
        m = 5
        tmpbuf = ["" for i in range(4)]
        while readbytes+4 <= n:
            m = read4(tmpbuf)
            buf[readbytes:readbytes+m]=tmpbuf
            readbytes+=m
            if m < 4:
                break
        if readbytes == n or m < 4:
            return readbytes
        tmpbuf = ["" for i in range(4)]
        m = min(read4(tmpbuf),n-readbytes)
        for i in range(m):
            buf[readbytes:readbytes+1] = tmpbuf[i]
            readbytes+=1
        return readbytes