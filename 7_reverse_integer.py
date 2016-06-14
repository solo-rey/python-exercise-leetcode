class Solution:
    # @return an integer
    def reverse(self, x):
        ret = 0
        b = x if x > 0 else -x
        while b > 0:
            if ret > 214748364:
                return 0
            ret = ret*10+b%10
            b /= 10
        return ret if x > 0 else -ret


s= Solution()
print s.reverse(-123)