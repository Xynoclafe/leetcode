"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def dfs(node, parent):
            if node == None:
                return None
            if node.left:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node.left = dfs(node.left, node)
                node.right = dfs(node.right, node)
            return node
        
        return dfs(root, None)