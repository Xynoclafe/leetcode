# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def inOrder(root, kList, k):
            if root == None:
                return
            inOrder(root.left, kList, k)
            if len(kList) >= k:
                return
            kList.append(root.val)
            if len(kList) >= k:
                return
            inOrder(root.right, kList, k)
            if len(kList) >= k:
                return
            return
        
        kList = []
        inOrder(root, kList, k)
        return kList[k-1]
