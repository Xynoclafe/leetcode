class LRUCache:

    def __init__(self, capacity: int):
        self.keyList = []
        self.valDict = {}
        self.currentLim = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.valDict.keys():
            self.keyList.remove(key)
            self.keyList.append(key)
            return self.valDict[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if(key in self.keyList):
            self.valDict[key] = value
            self.keyList.remove(key)
            self.keyList.append(key)
        elif(self.currentLim == self.capacity):
            remVal = self.keyList.pop(0)
            self.valDict.pop(remVal)
            self.keyList.append(key)
            self.valDict[key] = value
        else:
            self.keyList.append(key)
            self.valDict[key] = value
            self.currentLim += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
