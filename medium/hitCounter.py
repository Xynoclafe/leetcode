class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeStampList = []
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.timeStampList.append(timestamp)
        while True:
            if self.timeStampList[0] < timestamp - 300:
                self.timeStampList.pop(0)
            else:
                break

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while True:
            if len(self.timeStampList) == 0:
                break
            if self.timeStampList[0] <= timestamp - 300:
                self.timeStampList.pop(0)
            else:
                break
        return len(self.timeStampList)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)