# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inOrder(node, inOrderList):
            if node == None:
                return
            inOrder(node.left, inOrderList)
            inOrderList.append(node.val)
            inOrder(node.right, inOrderList)
            return
        
        inOrderList = []
        inOrder(root, inOrderList)
        return inOrderList
            
