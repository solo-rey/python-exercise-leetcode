class Solution:
    # @return a string
    def convertToTitle(self, num):
        ans = ""
        while num:
            ans = chr(ord('A')+(num-1) % 26) + ans
            num = (num-1)/26
        return ans