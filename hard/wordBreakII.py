from collections import defaultdict

class node:
            
    def __init__(self, val):
        self.val = val
        self.parents = []
        self.children = []
    
    def __str__(self):
        retStr = str(self.val)
        for child in self.children:
            retStr += "[ " + str(child) + " ]"
        return retStr

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def findPath(node, inList):
            if len(node.parents) == 0:
                inList.append(node.val)
                return [inList], 1
            paths = []
            for parent in node.parents:
                currentPaths, numPaths = findPath(parent, inList.copy())
                for i in range(numPaths):
                    currentPaths[i].append(node.val)
                    paths.append(currentPaths[i])
                num = len(paths)
            return paths, num
        
        wordSet = set(wordDict)
        nodeDict = defaultdict(int)
        
        visited = set({})
        l1 = []
        l2 = []
        l1.append(0)
        root = node(0)
        nodeDict[0] = root
        
        while len(l1) > 0:
            i = l1.pop(0)
            for j in range(i, len(s)):
                if s[i:j + 1] in wordSet and j + 1 not in visited:
                    l2.append(j + 1)
                    visited.add(j + 1)
                    nodeDict[j + 1] = node(j + 1)
                    nodeDict[i].children.append(nodeDict[j+1])
                    nodeDict[j + 1].parents.append(nodeDict[i])
                elif s[i:j + 1] in wordSet and j + 1 in visited:
                    nodeDict[i].children.append(nodeDict[j+1])
                    nodeDict[j + 1].parents.append(nodeDict[i])

            if len(l1) == 0:
                l1 = l2
                l2 = []

        length = len(s)
        returnList = []
        if length in visited:
            paths, num = findPath(nodeDict[length], [])
            for x in range(num):
                newList = []
                for i in range(len(paths[x]) - 1):
                    newList.append(s[paths[x][i]:paths[x][i+1]])
                returnList.append(' '.join(newList))
            return (returnList)
        else:
            return []
        
