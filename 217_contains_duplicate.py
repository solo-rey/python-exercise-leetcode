"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_map = {}
        for num in nums:
          if num not in num_map:
            num_map[num] = True
          else:
            return True
        return False

    def containsDuplicate1(self, nums):
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False



s = Solution()
print s.containsDuplicate([1, 2])