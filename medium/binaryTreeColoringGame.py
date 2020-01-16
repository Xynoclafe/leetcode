# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        
        neighbors = defaultdict(list)
        maxPossible = defaultdict(int)
        
        def findChildren(node):
            if node == None:
                return 0
            else:
                left = findChildren(node.left)
                right = findChildren(node.right)
                if left:
                    neighbors[node.val] += neighbors[node.left.val]
                if right:
                    neighbors[node.val] += neighbors[node.right.val]
                neighbors[node.val].append(node.val)
                maxPossible[node.val] = left + right + 1
                return left + right + 1
        
        findChildren(root)
        maxNodes = maxPossible[x]
        for index in maxPossible:
            if index != x:
                if maxPossible[index] > maxNodes:
                    if x not in neighbors[index]:
                        return True
                    elif maxPossible[index] - maxNodes > maxNodes:
                        return True
                elif index in neighbors[x] and maxPossible[index] > n - maxPossible[index]:
                    return True
        return False