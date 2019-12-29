"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def postOrder(node, postOrderList):
            if node == None:
                return
            for i in range(len(node.children)):
                postOrder(node.children[i], postOrderList)
            postOrderList.append(node.val)
            return
        
        postOrderList = []
        postOrder(root, postOrderList)
        return postOrderList
