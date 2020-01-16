# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        
        length = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:length + 1], post[:length])
        root.right = self.constructFromPrePost(pre[length + 1:], post[length:-1])
        return root