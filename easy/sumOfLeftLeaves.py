# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def dfs(node, left):
            
            if (node.left == node.right == None) and left:
                return node.val
            
            leftSum = 0
            
            if node.left:
                leftSum += dfs(node.left, True)
            if node.right:
                leftSum += dfs(node.right, False)
            
            return leftSum
        
        if root == None:
            return 0
        else:
            return dfs(root, False)
