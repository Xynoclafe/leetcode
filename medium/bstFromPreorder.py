# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def construct(preorder, maxm, minm):
            if len(preorder) > 0:
                child = preorder[0]
                if child > maxm or child < minm:
                    return None
                child = preorder.pop(0)
                node = TreeNode(child)
                node.left = construct(preorder, child, minm)
                node.right = construct(preorder, maxm, child)
                return node
            else:
                return None
                
        return construct(preorder, 10 ** 10, - (10 ** 10))
        