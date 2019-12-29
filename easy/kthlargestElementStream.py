class KthLargest:

    import heapq
    
    def __init__(self, k: int, nums: List[int]):
        self.numbers = [i for i in nums]
        self.k = k
        heapq.heapify(self.numbers)
        while(len(self.numbers) > self.k):
            heapq.heappop(self.numbers)

    def add(self, val: int) -> int:
        heapq.heappush(self.numbers, val)
        if (len(self.numbers) > self.k):
            heapq.heappop(self.numbers)
        return self.numbers[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
