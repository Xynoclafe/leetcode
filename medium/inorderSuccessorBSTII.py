"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        
        if node is None or (node.right is None and node.parent is None):
            return None
        
        elif node.right is None:
            curVal = node.val
            givenNode = node
            node = node.parent
            while node:
                prev = node
                if node.val > curVal:
                    return node
                node = node.parent
            node = prev.right
            while node:
                if node.val > curVal:
                    while (node or node.val > curVal):
                        prev = node
                        node = node.left
                    return prev if prev != givenNode else None
                prev = node
                node = node.right
            return prev if prev != givenNode else None
                    
        
        else:
            node = node.right
            while node:
                prev = node
                node = node.left
            return prev
