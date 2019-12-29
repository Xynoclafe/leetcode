# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        if length == 0:
            return None
        if length % 2 == 1:
            index = (length - 1) // 2
        else:
            index = (length) // 2
        #print(index)
        left = nums[:index]
        right = nums[index + 1:length]
        #print(nums[index], left, right)
        node = TreeNode(nums[index])
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)
        return node
