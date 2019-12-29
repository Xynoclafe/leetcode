"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    import copy
    def copyRandomList(self, head: 'Node') -> 'Node':
        copyLinks= {}
        copyHead = copy.deepcopy(head)
        copyLinks[head] = copyHead
        node = head
        newNode = copyHead
        while(node is not None):
            if(node.next is None):
                newNode.next = None
            elif(node.next in copyLinks.keys()):
                newNode.next = copyLinks[node.next]
            else:
                newNode.next = Node(node.next.val, node.next.next, node.next.random)
                copyLinks[node.next] = newNode.next
            
            if(node.random is None):
                newNode.random = None
            elif(node.random in copyLinks.keys()):
                newNode.random = copyLinks[node.random]
            else:
                newNode.random = Node(node.random.val, node.random.next, node.random.random)
                copyLinks[node.random] = newNode.random
            
            node = node.next
            newNode = newNode.next
        return copyHead
