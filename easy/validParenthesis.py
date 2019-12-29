class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if character in ["(", "{", "["]:
                stack.append(character)
            else:
                if len(stack) == 0:
                    return False
                elif character == ")":
                    char = stack.pop()
                    if(char != "("):
                        return False
                elif character == "}":
                    char = stack.pop()
                    if(char != "{"):
                        return False
                elif character == "]":
                    char = stack.pop()
                    if(char != "["):
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
        
