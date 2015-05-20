class Solution:
    """
    Given two binary strings, return their sum (also a binary string).

    For example,
    a = "11"
    b = "1"
    Return "100".
    """
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary_cheat(self, a, b):
        return bin(int(a, 2) + int(b, 2)).split('b')[1]

    def addBinary(self, a, b):
    	"""Sometimes built-in function cheats too much.
    	"""
        res, carry, len_a, len_b, i = "", 0, len(a), len(b), 0
        for i in range(max(len_a,len_b)):
            sum_x = carry
            if i< len_a:
                sum_x += int(a[-(i+1)])
            if i< len_b:
                sum_x += int(b[-(i+1)])
            carry = sum_x / 2
            sum_x = sum_x%2
            res = "{0}{1}".format(sum_x,res)
        if carry > 0:
            res = "1"+res
        return res
