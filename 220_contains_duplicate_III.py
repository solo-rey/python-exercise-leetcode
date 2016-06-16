"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference
between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        num_map = {}
        for i in range(len(nums)):
            if nums[i] not in num_map:
                num_map[nums[i]] = i
            else:
                if i - num_map[nums[i]] <= k and abs(nums[i]):
                    return True
                else:
                    num_map[nums[i]] = i
        return False