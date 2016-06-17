"""
Given an integer, write a function to determine if it is a power of two.
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n % 2 != 0 or n == 0:
            return False
        return self.isPowerOfTwo(n / 2)