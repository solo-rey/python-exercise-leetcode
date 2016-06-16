"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret_lst = []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        start, end = 0, 0
        for i in range(1, len(nums)):
            tmp_num = nums[i]
            if tmp_num-nums[i-1] == 1:
                end = i
            else :
                if start != end:
                    st = str(nums[start]) + "->" + str(nums[end])
                else:
                    st = str(nums[start])
                ret_lst.append(st)
                start, end = i, i
        if start != end:
            st = str(nums[start]) + "->" + str(nums[end])
        else:
            st = str(nums[start])
        ret_lst.append(st)
        return ret_lst


s = Solution()
print s.summaryRanges([0,1,2,4,5])
