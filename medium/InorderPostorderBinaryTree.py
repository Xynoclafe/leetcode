# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def construct(preorder, subTree):
            val = preorder[0] if len(subTree) > 0 else None
            if val in subTree:
                val = preorder.pop(0)
                index = subTree.index(val)
                node = TreeNode(val)
                lsTree = subTree[:index]
                rsTree = subTree[index + 1:] if index < len(subTree) - 1 else []
                node.left = construct(preorder, lsTree)
                node.right = construct(preorder, rsTree)
                return node
            else:
                return None
        
        return construct(preorder, inorder)