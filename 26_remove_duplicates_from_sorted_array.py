# class Solution:
#     # @param a list of integers
#     # @return an integer
#     """
#     Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
#     Do not allocate extra space for another array, you must do this in place with constant memory.
#
#     For example,
#     Given input array A = [1,1,2],
#
#     Your function should return length = 2, and A is now [1,2].
#     """
#     def removeDuplicates(self, A):
#         if not A:
#             return 0
#         if len(A) == 1:
#             return 1
#         index = 0
#         for i in range(1,len(A)):
#             if A[index] != A[i]:
#                 index+=1
#                 A[index] = A[i]
#         return index+1

"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 1:
            return len(nums)
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j+=1
        return j

s = Solution()
print s.removeDuplicates([1,1,2])

