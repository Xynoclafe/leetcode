# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        def findDepth(node):
            depth = 0
            while node.left:
                node = node.left
                depth += 1
            return depth
        
        def exists(index, depth, node):
            left = 0
            right = 2 ** depth - 1
            for _ in range(depth):
                pivot = (left + right) // 2
                if index <= pivot:
                    node = node.left
                    right = pivot
                else:
                    node = node.right
                    left = pivot  + 1
            return node is not None
        
        if not root:
            return 0
        depth = findDepth(root)
        if depth == 0:
            return 1
            
        left = 1
        right = 2 ** depth - 1
        while left <= right:
            pivot = (left + right) // 2
            if exists(pivot, depth, root):
                left = pivot + 1
            else:
                right = pivot - 1
        return (2 ** depth - 1) + left
            