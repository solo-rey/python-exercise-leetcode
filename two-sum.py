class Solution:
    """
    Given an array of integers, find two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

    You may assume that each input would have exactly one solution.

    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2
    """
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i, e in enumerate(num):
            if e in d:
                return d[e] + 1, i + 1
            d[target - e] = i

    def twoSum1(self, num, target):
        d = {}
        for i, e in enumerate(num):
            if target - e in d:
                return d[target - e] + 1, i + 1
            d[e] = i

    def twoSum2(self,num,target):
        dic={}
        for i in range(len(num)):
            if num[i] not in dic:
                dic[target-num[i]]=i+1
            else:
                return (dic[num[i]],i+1)
