# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        def constTree(nums, start, end):
        
            if len(nums[start:end]) == 0:
                return None
            rootVal = max(nums[start:end])
            rootIndex = index[rootVal]
        
            node = TreeNode(rootVal)
        
            if rootIndex > start:
                node.left = constTree(nums, start, rootIndex)
            
            if rootIndex < end:
                node.right = constTree(nums, rootIndex + 1, end)
        
            if rootIndex == start:
                node.left = None
        
            if rootIndex == end:
                node.right = None
        
            return node
        
        index = defaultdict(lambda: -1)
        
        for i in range(len(nums)):
            index[nums[i]] = i
        
        return constTree(nums, 0, len(nums))
