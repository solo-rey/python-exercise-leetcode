class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.dict = {}


    # @return nothing
    def add(self, number):
        if number not in self.dict:
            self.dict[number] = 1
        else:
            self.dict[number]+=1


    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        for i in self.dict.keys():
            if value-i in self.dict.keys():
                return True
        return False
