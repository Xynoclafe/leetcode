class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        count = 0
        j = length - 1
        while(j > -1 and nums[j] == val):
            count += 1
            j -= 1
        i = 0
        
        while i <= j:
            if nums[i] == val:
                count += 1
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                while(nums[j] == val):
                    count += 1
                    j -= 1
            i += 1
        
        return length - count