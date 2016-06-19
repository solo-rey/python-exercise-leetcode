"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

# class Solution:
#     # @param {integer[]} nums
#     # @return {string}
#     def cmp_str(self, x, y):
#         t1 = str(x) + str(y)
#         t2 = str(y) + str(x)
#         return t1 - t2
#     def largestNumber(self, nums):
#         sorted(nums, cmp=cmp_str)
#         t = ""
#         for i in reversed(range(len(nums))):
#             t += str(nums[i])
#         return t
#         # if t == '0':
#         #     return "0"
#         # else:
#         #     return t
#
#
# s = Solution()
# print s.largestNumber([2,1])