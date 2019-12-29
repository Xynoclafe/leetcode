# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        def dfs(node, target, items):
            if node == None:
                return False
            if items[target - node.val] != 0:
                return True
            else:
                items[node.val] = 1
                left = dfs(node.left, target, items)
                right = dfs(node.right, target, items)
                return left or right
        
        items = defaultdict(int)
        return dfs(root, k, items)
