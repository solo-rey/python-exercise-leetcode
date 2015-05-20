class LRUCache_other:
    # @param capacity, an integer
    def __init__(self, capacity):
        LRUCache.Dict = collections.OrderedDict()
        LRUCache.capacity = capacity
        LRUCache.numItems = 0

    # @return an integer
    def get(self, key):
        try:
            value = LRUCache.Dict[key]
            del LRUCache.Dict[key]
            LRUCache.Dict[key] = value
            return value
        except:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            del LRUCache.Dict[key]
            LRUCache.Dict[key] = value
            return
        except:
            if LRUCache.numItems == LRUCache.capacity:
                LRUCache.Dict.popitem(last = False)
                LRUCache.numItems -= 1
            LRUCache.Dict[key] = value
            LRUCache.numItems += 1
        return


class LRUCache_v2:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.dict = collections.OrderedDict() #key:ordered dictionary
        self.capacity = capacity
        self.numItems = 0


    # @return an integer
    def get(self, key):
        if key in self.dict:
            value = self.dict[key]
            del self.dict[key]
            self.dict[key] = value
            return value
        else:
            return -1


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.dict:
                del self.dict[key]
                self.dict[key] = value
                return
        else:
            if self.numItems < self.capacity:
                self.dict[key] = value
                self.numItems+=1
            else:
                self.dict.popitem(last = False)
                self.numItems-=1
                del self.dict[key]
                self.dict[key]=value
                self.numItems+=1


