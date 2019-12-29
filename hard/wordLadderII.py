from collections import defaultdict
class node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.parents = []
        
    def __str__(self):
        retStr = "[ " + self.val + " "
        for parent in self.parents:
            retStr += parent.__str__()
        retStr += " ]"
        return(retStr)

class Solution:    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
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
        
        
        if endWord not in wordList:
            return []
        
        if beginWord in wordList:
            wordList.remove(beginWord)
            
        startNode = node(beginWord)
        
        nodeList = defaultdict(lambda: None)
        nodeList[beginWord] = startNode
        
        allTypesDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                allTypesDict[word[0:i] + "*" + word[i+1:]].append(word)
        
        wordLevels = []
        wordLevels.append([beginWord])
        level = 1
        while(len(wordList) > 0):
            prevWords = wordLevels[level -1]
            curList = []
            for word in prevWords:
                nextLevel = []
                for i in range(len(word)):
                    nextLevel = nextLevel + allTypesDict[word[0:i] + "*" + word[i + 1:]]
                nextLevel = list(set(wordList).intersection(set(nextLevel)))
                for tWord in nextLevel:
                    if nodeList[tWord] == None:
                        nodeList[tWord] = node(tWord)
                    nodeList[tWord].parents.append(nodeList[word])
                    nodeList[word].children.append(nodeList[tWord])
                    curList.append(tWord)
            wordLevels.append(list(set(curList)))
            wordList = list(set(wordList) - set(curList))
            if endWord in curList:
                break
            if len(curList) == 0 and len(wordList) != 0:
                return []
            level += 1
        paths, num = findPath(nodeList[endWord], [])
        return paths
        
        
