import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)
        self.length = 0
        

    def balanceHeaps(self):
        while(abs(len(self.minHeap) - len(self.maxHeap)) > 1):
            if len(self.minHeap) > len(self.maxHeap):
                element = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -element)
            else:
                element = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -element)
            
    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0 or -num >= self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        self.balanceHeaps()
        self.length += 1

    def findMedian(self) -> float:
        if self.length % 2 == 1:
            return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else - self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
