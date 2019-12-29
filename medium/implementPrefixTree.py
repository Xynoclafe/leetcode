class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = "HEAD"
        self.children = []
        self.childList = []
        self.parent = None
    
    def letterNodes(self, value, parent):
        curNode = Trie()
        curNode.val = value
        curNode.parent = parent
        curNode.children = []
        return curNode

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        charList = [char for char in word]
        node = self
        for char in charList:
            if char not in node.childList:
                curNode = self.letterNodes(char, node)
                node.children.append(curNode)
                node.childList.append(char)
                node = curNode
            else:
                index = node.childList.index(char)
                node = node.children[index]
        node.children.append(self.letterNodes("END", node))
        node.childList.append("END")
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        charList = [char for char in word]
        for char in charList:
            if char in node.childList:
                index = node.childList.index(char)
                node = node.children[index]
            else:
                return False
        if "END" in node.childList:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        charList = [char for char in prefix]
        for char in charList:
            if char in node.childList:
                index = node.childList.index(char)
                node = node.children[index]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
