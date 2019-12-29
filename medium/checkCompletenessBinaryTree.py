# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        levels = []
        l1 = [root]
        l2 = []
        levels.append(l1.copy())
        
        while(len(l1) > 0):
            node = l1.pop(0)
            
            if node != None:
                l2.append(node.left)
                l2.append(node.right)
            
            if len(l1) == 0:
                if len(l2) != 0:
                    levels.append(l2.copy())
                l1 = l2
                l2 = []
            
        
        for i in range(len(levels) - 1):
            if len(levels[i]) != 2 ** i:
                return False
        if len(levels) == 1:
            return True
        
        flag = False
        for element in levels[-2]:
            print(element, flag)
            if element is None:
                flag = True
            elif element != None and flag:
                return False
            
        return True
