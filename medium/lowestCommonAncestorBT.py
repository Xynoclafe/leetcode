# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def bfs(node):
            node.parent = None
            l1 = [node]
            l2 = []
            visited = []
            level = 0
            while(len(l1) > 0):
                curNode = l1.pop(0)
                curNode.level = level
                visited.append(curNode)
                if curNode.left is not None and curNode.left not in visited:
                    curNode.left.parent = curNode
                    l2.append(curNode.left)
                if curNode.right is not None and curNode.right not in visited:
                    curNode.right.parent = curNode
                    l2.append(curNode.right)
                if curNode.parent is not None and curNode.parent not in visited:
                    l2.append(curNode.parent)
                if(len(l1) == 0):
                    l1 = l2
                    l2 = []
                    level += 1
        
        def findAncestor(p, q):
            pLevel = p.level
            qLevel = q.level
            diff = abs(pLevel - qLevel)
            if (pLevel > qLevel):
                for i in range(diff):
                    p = p.parent
            else:
                for i in range(diff):
                    q = q.parent
            if p == q:
                return p
            else:
                while(True):
                    p = p.parent
                    q = q.parent
                    if(p == q):
                        return p

                
        bfs(root)
        return findAncestor(p, q)
