"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        def nextLevel(node):
            while node:
                if node.child:
                    endNode = nextLevel(node.child)
                    endNode.next = node.next
                    if node.next:
                        endNode.next.prev = endNode
                    node.next = node.child
                    node.child.prev = node
                    node.child = None
                    node = endNode.next
                    if not node:
                        return endNode
                else:
                    if node.next:
                        node = node.next
                    else:
                        return node
        
        nextLevel(head)
        return head