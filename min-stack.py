
class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, x):
        if len(self.s2)==0 or x <= self.getMin():
            self.s2.append(x)
        self.s1.append(x)


    # @return nothing
    def pop(self):
        value = self.s1[-1]
        self.s1.pop()
        if value == self.getMin():
            self.s2.pop()


    # @return an integer
    def top(self):
        return self.s1[-1]


    # @return an integer
    def getMin(self):
        return self.s2[-1]

s = MinStack()
s.push(-1)
print s.top()
print s.getMin()

"""
s.push(2)
s.push(10)
s.push(5)
s.push(1)
print s.getMin()
print s.top()
s.pop()
print s.getMin()
"""