class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [set({}) for _ in range(2017)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        mapKey = key % 2017
        existSet = self.map[mapKey]
        for pair in existSet:
            if pair[0] == key:
                self.map[mapKey].remove((key, pair[1]))
                break
        self.map[mapKey].add((key, value))
        return
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        mapKey = key % 2017
        existSet = self.map[mapKey]
        for pair in existSet:
            if pair[0] == key:
                return pair[1]
        
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        mapKey = key % 2017
        existSet = self.map[mapKey]
        
        for pair in existSet:
            if pair[0] == key:
                self.map[mapKey].remove((key, pair[1]))
                break
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)