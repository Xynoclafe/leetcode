class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fp = 0
        cp = 0
        sp = len(nums) - 1
        
        while cp <= sp:
            if nums[cp] == 0:
                nums[fp], nums[cp] = nums[cp], nums[fp]
                cp += 1
                fp += 1
            elif nums[cp] == 2:
                nums[sp], nums[cp] = nums[cp], nums[sp]
                sp -= 1
            else:
                cp += 1
