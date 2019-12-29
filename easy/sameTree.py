# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def listNodes(self, node, nodeList):
        if node is None:
            nodeList.append(None)
        else:
            nodeList.append(node.val)
            self.listNodes(node.left, nodeList)
            self.listNodes(node.right, nodeList)
        return
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        nodeListP = []
        nodeListQ = []
        self.listNodes(p, nodeListP)
        self.listNodes(q, nodeListQ)
        print(nodeListP, nodeListQ)
        if nodeListP == nodeListQ:
            return True
        else:
            return False
        
