# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def isPalindrome(l):
            if len(l) == 0:
                return True
            i = 0
            j = len(l) - 1
            
            while(i < j):
                if l[i] == l[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        
        l1 = [root]
        l2 = []
        l2Vals = []
        while(len(l1) > 0):
            node = l1.pop(0)
            if node is not None:
                l2.append(node.left)
                if node.left:
                    l2Vals.append(node.left.val)
                else:
                    l2Vals.append(None)
                l2.append(node.right)
                if node.right:
                    l2Vals.append(node.right.val)
                else:
                    l2Vals.append(None)
            if len(l1) == 0:
                if not isPalindrome(l2Vals):
                    return False
                else:
                    l1 = l2
                    l2 = []
                    l2Vals = []
                
        return True