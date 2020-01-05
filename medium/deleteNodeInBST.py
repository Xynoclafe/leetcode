# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        def find(node, target):
            if node == None:
                return node
            
            elif node.val == target:
                
                if node.left == None:
                    node = node.right
                    return node
            
                elif node.right == None:
                    node = node.left
                    return node
        
                else:
                    node.right = findSuccessor(node, node.right)
                    return node
                
                
            if node.val < target:
                node.right = find(node.right, target)
            else:
                node.left = find(node.left, target)
            return node
        
        def findSuccessor(target, node):
            if node.left is None:
                target.val = node.val
                node = node.right
                return node
            else:
                node.left = findSuccessor(target, node.left)
                return node
        
        return find(root, key)