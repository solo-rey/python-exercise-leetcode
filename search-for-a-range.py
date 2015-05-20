class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if A is None:
            return (-1,-1)
        l,r=0,len(A)-1
        mid = -1
        while l <= r:
            mid=(l+r) / 2
            if A[mid] == target:
                break
            elif A[mid] > target:
                r=mid-1
            elif A[mid] < target:
                l=mid+1
        if A[mid] != target:
            return [-1,-1]
        start,end=mid,mid
        l,r,m=mid,len(A)-1,mid
        while l <= r:
            m=(l+r)/2
            if A[m] == target:
                l=m+1
            elif A[m] > target:
                r=m-1
        end=r
        l,r,m=0,mid,mid
        while l <= r:
            m=(l+r)/2
            if A[m] == target:
                r=m-1
            elif A[m] < target:
                l=m+1
        start = l
        return [start,end]


s= Solution()
print s.searchRange([1,2,3,3,3,3,4,5,9], 3)




