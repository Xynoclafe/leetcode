# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class graphNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def getGraph(self, root, parent, newNode, target):
        if(root is not None):
            newRoot = graphNode(root.val)
            newRoot.parent = parent
            newRoot.left, newNode = self.getGraph(root.left, newRoot, newNode, target)
            newRoot.right, newNode = self.getGraph(root.right, newRoot, newNode, target)
            if root == target:
                newNode = newRoot
                print(newNode)
            return newRoot, newNode
        else:
            return None, newNode

    def bfs(self, target, k):
        l1 = [target]
        l2 = []
        visited = []
        level = 0
        while(len(l1) > 0):
            curNode = l1.pop(0)
            visited.append(curNode)
            print(curNode.val)
            if curNode.left is not None and curNode.left not in visited:
                l2.append(curNode.left)
            if curNode.right is not None and curNode.right not in visited:
                l2.append(curNode.right)
            if curNode.parent is not None and curNode.parent not in visited:
                l2.append(curNode.parent)
            if(len(l1) == 0):
                l1 = l2
                l2 = []
                level += 1
                if level == k:
                    retList = []
                    for item in l1:
                        retList.append(item.val)
                    return retList
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if K == 0:
            return [target.val]
        newRoot, newNode = self.getGraph(root, None, None, target)
        retList = self.bfs(newNode, K)
        if retList is None:
            return []
        else:
            return retList
