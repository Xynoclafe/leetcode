# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        if len(nums) == 0:
            return None
        
        rootVal = max(nums)
        rootIndex = (nums.index(rootVal))
        
        node = TreeNode(rootVal)
        
        if rootIndex > 0:
            node.left = self.constructMaximumBinaryTree(nums[:rootIndex])
            
        if rootIndex < len(nums) - 1:
            node.right = self.constructMaximumBinaryTree(nums[rootIndex + 1:])
        
        if rootIndex == 0:
            node.left = None
        
        if rootIndex == len(nums) - 1:
            node.right = None
        
        return node
