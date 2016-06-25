"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        for i in range(32):

            if n & 1 == 1:
                a = (a << 1) + 1
            else:
                a = a << 1
            print "{0:b}".format(a)
            n = n >> 1
        return a

s = Solution()
print s.reverseBits(43261596)