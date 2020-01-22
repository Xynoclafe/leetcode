import random
class Solution:

    def __init__(self, w: List[int]):
        self.runningSum = 0
        self.sumList = []
        for num in w:
            self.runningSum += num
            self.sumList.append(self.runningSum)

    def pickIndex(self) -> int:
        num = random.choice(range(self.runningSum))
        return bisect.bisect(self.sumList, num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
