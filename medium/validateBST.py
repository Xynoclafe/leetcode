# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        
        def inOrderT(root, inOrder):
            if root == None:
                return
            inOrderT(root.left, inOrder)
            inOrder.append(root.val)
            inOrderT(root.right, inOrder)
        
        
        inOrder = []
        inOrderT(root, inOrder)
        
        for i in range(len(inOrder) - 1):
            if inOrder[i] >= inOrder[i + 1]:
                return False
        return True
