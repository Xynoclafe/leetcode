from random import choice
class Solution:

    def __init__(self, w: List[int]):
        self.nums = []
        self.pSum = 0
        for i in range(len(w)):
            self.pSum += w[i]
            self.nums.append(self.pSum)

    def pickIndex(self) -> int:
        choose = choice(range(self.pSum))
        
        low = 0
        high = len(self.nums) - 1
        while(low != high):
            mid = (low + high) // 2
            if choose >= self.nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()