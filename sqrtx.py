class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt1(self, x):
        left,right = 0,x
        while right >= left:
            mid = (right+left) / 2
            if mid*mid == x:
                return mid
            elif x < mid*mid:
                right = mid-1
            else:
                left = mid+1
        return right

    def sqrt(self, x):
        low, high = 0, x
        while high >= low:
            mid = (high + low) / 2
            if x < mid * mid:
                high = mid - 1
            else:
                low = mid + 1
        return int(high)

s = Solution()
print s.sqrt1(2)