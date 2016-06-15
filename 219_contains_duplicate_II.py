"""
Given an array of integers and an integer k, find out whether
there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_map = {}
        for i in range(len(nums)):
            if nums[i] not in num_map:
                num_map[nums[i]] = i
            else:
                if i - num_map[nums[i]] <= k:
                    return True
                else:
                    num_map[nums[i]] = i
        return False



s = Solution()
print s.containsNearbyDuplicate([1, 2, 3, 1], 4)