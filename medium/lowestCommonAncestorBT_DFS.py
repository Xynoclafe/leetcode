# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(p,q, root):
            if root == None:
                return False, False, None
            else:
                left = dfs(p, q, root.left)
                right = dfs(p, q, root.right)
                if (left[0] or right[0]) and (left[1] or right[1]):
                    if not (left[0] and left[1]) and not (right[0] and right[1]):
                        return True, True, root
                    else:
                        return (left[0] or right[0]), (left[1] or right[1]), (left[2] or right[2])
                elif (left[0] or right[0]):
                    if root == q:
                        return True, True, root
                    else:
                        return True, False, None
                elif (left[1] or right[1]):
                    if root == p:
                        return True, True, root
                    else:
                        return False, True, None
                else:
                    if root == p:
                        return True, False, None
                    elif root == q:
                        return False, True, None
                    else:
                        return False, False, None
                
        
        return dfs(p, q, root)[2]
