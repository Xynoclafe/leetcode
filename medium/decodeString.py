class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        no = ""
        for i in range(len(s)):
            if s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                no = no + s[i]
            elif s[i] != "]":
                if no != "":
                    stack.append(no)
                    no = ""
                stack.append(s[i])
            else:
                curString = []
                flag = True
                while flag:
                    char = stack.pop()
                    if char == "[":
                        flag = False
                    else:
                        curString.append(char)
                number = int(stack.pop())
                curString = curString[::-1]
                string = ''.join(char for char in curString)
                stack.append(number * string)
        return (''.join(char for char in stack))