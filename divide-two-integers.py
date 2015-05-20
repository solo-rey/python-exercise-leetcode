class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if dividend == 0 or divisor == 0:
            return 0
        isNeg = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        a = abs(dividend)
        b = abs(divisor)
        if b > a:
            return 0
        sum,pow,result = 0,0,0
        while a >= b:
            pow = 1
            sum = b
            while sum+sum <= a:
                sum += sum
                pow += pow
            a -= sum
            result += pow

        return result if not isNeg else -result

