# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        
        def dfsSum(node, targetSum, prevSum, curList, listOfLists):

            currentSum = prevSum + node.val
            curList.append(node.val)
            
            if node.left == None and node.right == None:
                if currentSum == targetSum:
                    listOfLists.append(curList.copy())
            
            left = right = False
            if node.left is not None:
                left = dfsSum(node.left, targetSum, currentSum, curList, listOfLists)
            if not left and node.right is not None:
                right = dfsSum(node.right, targetSum, currentSum, curList, listOfLists)
            curList.pop()
            return
        
        if root == None:
            return []
        
        listOfLists = []
        dfsSum(root, sum, 0, [], listOfLists)
        return listOfLists
