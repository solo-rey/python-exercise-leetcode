class Solution:
    # @return a string
    def getPermutation(self, n, k):
        k-=1
        num = []
        for i in range(1,n+1):
            num.append(i)
        factorial = 1
        for i in range(2,n):
            factorial*=i
        res=""
        time = n-1
        while time>=0:
            index = k/factorial
            res+=str(num[index])
            num.pop(index)
            k%=factorial
            if time != 0:
                factorial/=time
            time-=1
        return res

