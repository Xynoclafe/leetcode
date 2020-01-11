# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None:
                return False
            if node2 is None:
                return False
            if node1.val != node2.val:
                return False
            
            left1 = dfs(node1.left, node2.left)
            right1 = dfs(node1.right, node2.right)
            left2 = dfs(node1.left, node2.right)
            right2 = dfs(node1.right, node2.left)
            
            return (left1 and right1) or (left2 and right2)
        
        return dfs(root1, root2)