class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        candidate,count = None,0
        for i in range(len(num)):
            if count == 0:
                candidate = num[i]
                count=1
            elif num[i] == candidate:
                count+=1
            else:
                count-=1
        return candidate