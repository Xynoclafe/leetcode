# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        def postOrder(node, postOrderList):
            if node == None:
                return
            postOrder(node.left, postOrderList)
            postOrder(node.right, postOrderList)
            postOrderList.append(node.val)
            return
        
        postOrderList = []
        postOrder(root, postOrderList)
        return postOrderList
