# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        if p is None:
            return None
        
        if p.right:
            node = p.right
            while node:
                prev = node
                node = node.left
            return prev
        
        if root.val <= p.val:
            node = root
            while node:
                prev = node
                node = node.right
                if node and node.val > p.val:
                    while node.val > p.val:
                        prev = node
                        node = node.left
                    return prev if prev != p else None
            return prev if prev != p else None
        
        if root.val > p.val:
            node = root
            while node:
                prev = node
                node = node.left
                if node and node.val == p.val:
                    return prev
                if node and node.val < p.val:
                    curPrev = prev
                    while node.val < p.val:
                        prev = node
                        node = node.right
                    if node and node.val > p.val:
                        return node
                    elif prev.val > p.val:
                        return prev
                    else:
                        return curPrev
            return prev
