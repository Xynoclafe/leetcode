class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product = 1
        negProd = 0
        for i in range(1,4):
            product *= nums[-i]
        if(nums[0] < 0):
            negProd = nums[0] * nums[1] * nums[-1]
        return max(negProd, product)
        
