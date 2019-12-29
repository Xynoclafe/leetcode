class TwoSum:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numList = []
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.numList.append(number)
        
        

    def find(self, value: int) -> bool:
        from collections import defaultdict
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        nums = defaultdict(int)
        for i in self.numList:
            if nums[value - i] == 0:
                nums[i] = 1
            else:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
