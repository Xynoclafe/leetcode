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
        
        l1 = [root]
        l2 = []
        while(len(l1) > 0):
            node = l1.pop(0)
            if node is not None:
                if node.left:
                    l2.append(node.left)
                if node.right:
                    l2.append(node.right)
            if len(l1) == 0:
                l1 = l2
                l2 = []
                for i in range(len(l1) - 1):
                    l1[i].next = l1[i + 1]
        
        return root
