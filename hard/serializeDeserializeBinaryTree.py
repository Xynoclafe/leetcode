# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def dfs2list(self, node, nodeList):
        if node == None:
            nodeList.append(None)
        else:
            nodeList.append(node.val)
            self.dfs2list(node.left, nodeList)
            self.dfs2list(node.right, nodeList)
        return
    
    def list2tree(self, nodeList):
        if(len(nodeList) == 0):
            return None
        x = nodeList.pop(0)
        if x is None:
            return None
        newNode = TreeNode(x)
        newNode.left = self.list2tree(nodeList)
        newNode.right = self.list2tree(nodeList)
        return newNode

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodeList = []
        self.dfs2list(root, nodeList)
        return str(nodeList)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodeList = eval(data)
        root = self.list2tree(nodeList)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
