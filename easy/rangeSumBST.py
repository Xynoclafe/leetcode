# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        def dfs(node, runningSum, L, R):
            if node == None:
                return runningSum
            if node.val >= L and node.val <= R:
                runningSum += node.val
                runningSum = dfs(node.left, runningSum, L, R)
                runningSum = dfs(node.right, runningSum, L, R)
            elif node.val < L:
                runningSum = dfs(node.right, runningSum, L, R)
            else:
                runningSum = dfs(node.left, runningSum, L, R)
            return runningSum
        
        return dfs(root, 0, L, R)
            