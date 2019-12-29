# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        def dfsSum(node, targetSum, prevSum):
            
            currentSum = prevSum + node.val
            
            if node.left == None and node.right == None:
                if currentSum == targetSum:
                    return True
                else:
                    return False
            
            left = right = False
            if node.left is not None:
                left = dfsSum(node.left, targetSum, currentSum)
            if not left and node.right is not None:
                right = dfsSum(node.right, targetSum, currentSum)
            return left or right
        
        if root == None:
            return False
        
        return dfsSum(root, sum, 0)
