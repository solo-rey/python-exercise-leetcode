class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer

    """
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.
    """

    """
    take-away:1. last = len(A); 2. should consider equal to corner case(A[start] <= target and target <= A[last-1])
    """
    def search(self, A, target):
        start = 0
        last = len(A)
        while start != last:
            mid = (start + last) / 2
            if A[mid] == target:
                return mid
            if A[start] <= A[mid]:
                if A[start] <= target and target < A[mid]:
                    last = mid
                else:
                    start = mid+1
            else:
                if A[mid] < target and target <= A[last-1]:
                    start = mid+1
                else:
                    last = mid
        return -1

