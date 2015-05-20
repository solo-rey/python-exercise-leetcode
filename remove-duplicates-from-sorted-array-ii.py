class Solution:
    # @param A a list of integers
    # @return an integer

    """
    Follow up for "Remove Duplicates":
    What if duplicates are allowed at most twice?

    For example,
    Given sorted array A = [1,1,1,2,2,3],

    Your function should return length = 5, and A is now [1,1,2,2,3].
    """
    def removeDuplicates(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return 1
        if len(A) == 2:
            return 2
        index = 0
        times = 0 #counter, < 2 is still ok
        for i in range(1,len(A)):
            if A[index] != A[i]:
                index+=1
                A[index] = A[i]
                times = 0
            else:
                if times < 1:
                    index+=1
                    A[index] = A[i]
                    times+=1
        return index+1


