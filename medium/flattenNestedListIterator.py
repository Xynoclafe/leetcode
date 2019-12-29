# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = []
        self.nestedList = nestedList
        
    
    def next(self) -> int:
        return self.queue.pop(0)
            
            
                
    
    def hasNext(self) -> bool:
        
        def flatten(NestedList):
            i = 0
            while len(NestedList.getList()) > 0:
                element = NestedList.getList()[0]
                if element.isInteger():
                    self.queue.append(element.getInteger())
                else:
                    flatten(element)
                NestedList.getList().pop(0)
        
        if len(self.queue) > 0:
            return True
        if len(self.nestedList) == 0:
            return False
        
        while len(self.nestedList) > 0:
            nextElement = self.nestedList[0]
        
            if nextElement.isInteger():
                self.queue.append(self.nestedList.pop(0))
                return True

            else:
                flatten(nextElement)
                self.nestedList.pop(0)
                if len(self.queue) > 0:
                    return True
                
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
