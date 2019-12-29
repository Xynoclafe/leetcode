# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def flatten(self, arr, node):
        if node is not None:
            self.flatten(arr, node.left)
            arr.append(node.val)
            self.flatten(arr, node.right)
        
    
    def __init__(self, root: TreeNode):
        self.arr = []
        self.flatten(self.arr, root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.arr.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.arr) > 0:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
