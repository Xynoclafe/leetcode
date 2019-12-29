from random import choice

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.permutable = nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.permutable = self.original.copy()
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        retList = self.permutable
        choiceList = [i for i in range(len(retList))]
        i = 0
        while(len(choiceList) > 0):
            num = choice(choiceList)
            retList[i] = self.original[num]
            i += 1
            choiceList.remove(num)
        return retList
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
