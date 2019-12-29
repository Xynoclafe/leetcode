# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isMatch(self, s, t):
        if(s == None and t == None):
            return True
        elif(s == None or t == None):
            return False
        if(s.val != t.val):
            return False
        else:
            flag1 = self.isMatch(s.left, t.left)
            flag2 = self.isMatch(s.right, t.right)
            return (flag1 and flag2)
        
    def findRoots(self, s, t):
        flag = False
        if s == None:
            return flag
        elif s.val == t.val:
            flag = self.isMatch(s, t)
        if flag:
            return flag
        else:
            flag1 = self.findRoots(s.left, t)
            flag2 = self.findRoots(s.right, t)
            if flag1 or flag2:
                return True
        return flag
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.findRoots(s, t)
