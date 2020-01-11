from collections import deque
class Solution:
    def expand(self, S: str) -> List[str]:
        returnList = [""]
        flag = False
        stack = deque([])
        for element in S:
            if element == ",":
                continue
            elif element == "{":
                stack.append(element)
                flag = True
            elif element == "}":
                flag = False
                elements = deque([])
                while len(stack) > 0:
                    char = stack.pop()
                    if char != "{":
                        elements.append(char)
                newList = []
                for i in range(len(returnList)):
                    for char in elements:
                        newList.append(returnList[i] + char)
                returnList = newList
            elif flag:
                stack.append(element)
            else:
                for i in range(len(returnList)):
                    returnList[i] += element
        
        return sorted(returnList)