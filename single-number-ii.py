
# @param A, a list of integer
# @return an integer
""" this could be used to calculate any k numbers(appear k times)"""
def singleNumber(A):
    digits = [0 for i in range(32)]
    for i in range(32):
        for j in range(len(A)):
            digits[i] += int(A[j]>>i & 1)
    res = 0
    for i in range(32):
        res += digits[i]%3 << i
    return res

def singleNumber(self, A):
    one, two, three = 0, 0, 0
    for i in range(len(A)):
        two |= one & A[i];
        one ^= A[i];
        three = one & two;
        one &= ~three;
        two &= ~three;
    return one

print singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
