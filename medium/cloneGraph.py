"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    import copy
    def copyNeighbors(self, node, copyDict):
        neighbors = []
        for neighbor in node.neighbors:
            if(neighbor in copyDict.keys()):
                neighbors.append(copyDict[neighbor])
            else:
                copyDict[neighbor] = Node(neighbor.val, None)
                neighbors.append(copyDict[neighbor])
                copyDict[neighbor].neighbors = self.copyNeighbors(neighbor, copyDict)
        return neighbors
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        copyDict = {}
        copyNode = Node(node.val, None)
        copyDict[node] = copyNode
        copyNode.neighbors = self.copyNeighbors(node, copyDict)
        return copyNode
        
