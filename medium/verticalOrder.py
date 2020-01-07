# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        verticalPos = defaultdict(list)
        l = [(root, 0)]
        
        while(len(l) > 0):
            node = l.pop(0)
            if node[0]:
                verticalPos[node[1]].append(node[0].val)
                if node[0].left:
                    l.append((node[0].left, node[1] - 1))
                if node[0].right:
                    l.append((node[0].right, node[1] + 1))
        
        return [verticalPos[i] for i in sorted(verticalPos)]