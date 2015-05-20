class Solution:
    """
    Given an array of integers, every element appears twice except for one. Find that single one.

    Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
    """
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        x = 0
        for i in range(len(A)):
            x^=A[i]
        return x
