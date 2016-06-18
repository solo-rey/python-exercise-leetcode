"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        t = num
        while t >= 10:
            num = t
            t = 0
            while num > 0:
                t += num % 10
                num /= 10
        return t

s = Solution()
print s.addDigits(38)