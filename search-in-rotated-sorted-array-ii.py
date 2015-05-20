class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean

    """
    Follow up for "Search in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

    Write a function to determine if a given target is in the array.
    """
    def search(self, A, target):
        start = 0
        last = len(A)
        while start != last:
            mid = (start + last) / 2
            if A[mid] == target:
                return True
            if A[start] < A[mid]:
                if A[start] <= target and target < A[mid]:
                    last = mid
                else:
                    start = mid+1
            elif A[mid] < A[last-1]:
                if A[mid] < target and target <= A[last-1]:
                    start = mid+1
                else:
                    last = mid
            else:
                start+=1
        return False