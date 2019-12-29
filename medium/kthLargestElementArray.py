class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsCopy = sorted(nums)
        return numsCopy[len(numsCopy) - k]
