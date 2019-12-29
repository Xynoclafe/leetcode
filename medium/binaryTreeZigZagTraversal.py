# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        
        def getVals(nodeList):
            retList = [node.val for node in nodeList]
            return retList
        
        if root is None:
            return []
            
        flag = False
        retList = []
        l1 = [root]
        l2 = []
        retList.append(getVals(l1))
        
        while(len(l1) > 0):
            node = l1.pop()
            if flag:
                if node.left is not None:
                    l2.append(node.left)
                if node.right is not None:
                    l2.append(node.right)
            else:
                if node.right is not None:
                    l2.append(node.right)
                if node.left is not None:
                    l2.append(node.left)
            if len(l1) == 0:
                flag = not flag
                l1 = l2
                if len(l1) > 0:
                    retList.append(getVals(l1))
                l2 = []
        return retList
