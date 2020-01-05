# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        def dfs(node, parent):
            if node == None:
                return True
            
            if node.val != parent:
                return False
            
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            
            return left and right
        
        return dfs(root, root.val)
        