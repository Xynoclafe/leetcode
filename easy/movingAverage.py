class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.index = 0
        self.window = [0] * size
        self.size = size
        self.movingSum = 0
        

    def next(self, val: int) -> float:
        self.movingSum += val
        curIndex = self.index % self.size
        self.movingSum -= self.window[curIndex]
        self.window[curIndex] = val
        self.index += 1
        if self.index < self.size:
            return self.movingSum/self.index
        else:
            return self.movingSum/self.size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)