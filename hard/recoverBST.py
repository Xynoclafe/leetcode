# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inOrder(node, inOrderList, dictionary):
            if node == None:
                return
            dictionary[node.val] = node
            inOrder(node.left, inOrderList, dictionary)
            inOrderList.append(node.val)
            inOrder(node.right, inOrderList, dictionary)
        
        dictionary = {}
        inOrderList = []
        inOrder(root, inOrderList, dictionary)
        
        lower = -1
        greater = -1
        
        for i in range(len(inOrderList) - 1):
            if inOrderList[i + 1] < inOrderList[i]:
                greater = inOrderList[i  + 1]
                if lower == -1:
                    lower = inOrderList[i]
                else:
                    break
            
            
        node1 = dictionary[lower]
        node2 = dictionary[greater]
        
        temp = node1.val
        node1.val = node2.val
        node2.val = temp
        
