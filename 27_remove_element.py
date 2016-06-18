# @param    A       a list of integers
# @param    elem    an integer, value need to be removed
#remove elements in place
# @return an integer
def removeElement(A, elem):
    if not A or len(A) == 0:
        return 0
    cur = 0
    for i in range(len(A)):
        if A[i] != elem:
            A[cur]=A[i]
            cur+=1
    return len(A[:cur])

print removeElement([2],3)


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
        return j