class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        l,r = 0,len(matrix)-1
        while l <= r:
            mid =(l+r)/2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                r=mid-1
            else:
                l=mid+1
        row = r
        if row < 0:
            return False
        l,r = 0,len(matrix[0])-1
        while l <= r:
            mid = (l+r)/2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                r = mid-1
            else:
                l=mid+1
        return False
