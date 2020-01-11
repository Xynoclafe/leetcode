from collections import deque
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        stack1 = deque([])
        stack2 = deque([])
        
        for char in S:
            if char != "#":
                stack1.append(char)
            if char == "#" and len(stack1) > 0:
                stack1.pop()
        
        for char in T:
            if char != "#":
                stack2.append(char)
            if char == "#" and len(stack2) > 0:
                stack2.pop()
        
        return True if stack1 == stack2 else False