# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        def dfs(node, to_delete, returnList):
            if node == None:
                return None, returnList
            node.left, returnList = dfs(node.left, to_delete, returnList)
            node.right, returnList = dfs(node.right, to_delete, returnList)
            
            if node.val in to_delete:
                if node.left:
                    returnList.append(node.left)
                if node.right:
                    returnList.append(node.right)
                node = None
            return node, returnList
            
            
        
        root, returnList = dfs(root, set(to_delete), [])
        
        if root:
            returnList.append(root)
        
        return returnList
        