"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

"""
Dynamic programming, dp, each record the max sum of that position house
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
          return 0
        if len(nums) == 1:
          return nums[0]
        if len(nums) == 2:
          return max(nums[0], nums[1])
        dp = [0 for i in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
          dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[len(nums)-1]

    def rob1(self, nums):
      if len(nums) == 0:
        return 0
      if len(nums) == 1:
        return nums[0]
      if len(nums) == 2:
        return max(nums[0], nums[1])
      a, b = 0, 0
      for i in range(len(nums)):
        if i % 2 == 0:
          a += nums[i]
          a = max(a, b)
        else:
          b += nums[i]
          b = max(a, b)
      return max(a,b)

s = Solution()
print s.rob([1,2,3])