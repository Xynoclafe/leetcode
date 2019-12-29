from collections import defaultdict
class Node:
    
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        self.visited = False

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        def dfs(node, parent):
            node.visited = True
            node.lowLink = node.val
            for neighbor in node.neighbors:
                if neighbor == parent:
                    continue
                if neighbor.visited:
                    if neighbor.lowLink < neighbor.val:
                        neighbor.lowLink = min(node.lowLink, neighbor.lowLink)
                    node.lowLink = min(node.lowLink, neighbor.lowLink)
                else:
                    dfs(neighbor, node)
                    if neighbor.lowLink < neighbor.val:
                        neighbor.lowLink = min(node.lowLink, neighbor.lowLink)
                    node.lowLink = min(node.lowLink, neighbor.lowLink)
                        
        
        nodes = defaultdict(int)
        
        
        for connection in connections:
            connection.sort()
            if nodes[connection[0]] == 0:
                nodes[connection[0]] = Node(connection[0])
            if nodes[connection[1]] == 0:
                nodes[connection[1]] = Node(connection[1])
            nodes[connection[0]].neighbors.append(nodes[connection[1]])
            nodes[connection[1]].neighbors.append(nodes[connection[0]])
        
        dfs(nodes[0], None)
        returnList = []
        
        for connection in connections:
            if nodes[connection[0]].lowLink != nodes[connection[1]].lowLink:
                returnList.append([connection[0], connection[1]])
        
        return (returnList)
