# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        if root == None or root.val == None:
            return []

        levels = deque([])
        l1 = deque([root])
        l2 = deque([])
        vals = deque([])
        
        while len(l1) > 0:
            node = l1.popleft()
            vals.append(node.val)
            if node.left:
                l2.append(node.left)
            if node.right:
                l2.append(node.right)
            if len(l1) == 0:
                if vals:
                    levels.appendleft(vals.copy())
                    vals = []
                l1 = l2
                l2 = deque([])
        
        return levels
                
