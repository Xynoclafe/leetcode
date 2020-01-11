# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        
        self.curMax = 0
        
        def dfs(node):
            if not node:
                return 0
            ldepth = dfs(node.left)
            rdepth = dfs(node.right)
            self.curMax = max(self.curMax, ldepth + rdepth)
            return max(ldepth, rdepth) + 1
        
        dfs(root)
        
        return self.curMax