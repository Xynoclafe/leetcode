class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArray = [0] * len(nums)
        rightArray = [0] * len(nums)
        ans = [0] * len(nums)
        
        i = 0
        j = len(nums) - 1
        curProduct = 1
        rCurProduct = 1
        while(i < len(nums)):
            if i > 0:
                curProduct *= nums[i - 1]
            leftArray[i] = (curProduct)
            i += 1
            
            if j < len(nums) - 1:
                rCurProduct *= nums[j + 1]
            rightArray[j] = (rCurProduct)
            j -= 1
        
        print(leftArray, rightArray)
        
        for i in range(len(nums)):
            ans[i] = (leftArray[i] * rightArray[i])
        
        return (ans)