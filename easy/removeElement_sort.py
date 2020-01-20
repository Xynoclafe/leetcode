class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) > 0:
            replaceVal = max(nums) + 1.5
        length = len(nums)
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
                nums[i] = replaceVal
        
        nums.sort()
        return length - count