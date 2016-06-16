"""
find out h-index
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if i+1 > citations[i]:
                return i
        return len(citations)


s = Solution()
print s.hIndex([3,0,6,1,5])
print s.hIndex([1])