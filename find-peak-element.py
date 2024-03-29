class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement1(self, num):
        size = len(num)
        return self.search(num, 0, size - 1)

    def search(self, num, start, end):
        if start == end:
            return start
        if start + 1 == end:
            return [start, end][num[start] < num[end]]
        mid = (start + end) / 2
        if num[mid] < num[mid - 1]:
            return self.search(num, start, mid - 1)
        if num[mid] < num[mid + 1]:
            return self.search(num, mid + 1, end)
        return mid


    def findPeakElement(self, num):
        if num is None:
            return 0
        low,high = 0, len(num)-1
        while low < high:
            mid1 = (low+high)/2
            mid2 = mid1+1
            if num[mid1] < num[mid2]:
                low = mid2
            else:
                high = mid1
        return low
