class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        signStack = []
        noStack = []
        no = 0.5
        for i in range(len(s)):
            if(s[i] == " "):
                continue
            elif(s[i] in ["+", "-", "("]):
                if(no != 0.5):
                    stack.append(no)
                    no = 0.5
                stack.append(s[i])
            elif(s[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
                if(no == 0.5):
                    no = 0
                no = no * 10 + int(s[i])
            elif(s[i] == ")"):
                if(no != 0.5):
                    stack.append(no)
                    no = 0.5
                #print(stack)
                while(len(stack) != 0 and stack[-1] != "("):
                    c = stack.pop()
                    if(c == "+" or c == "-"):
                        signStack.append(c)
                    else:
                        noStack.append(c)
                if(len(stack) > 0):
                    if(stack[-1] == "("):
                        stack.pop()
                no1 = 0.5
                while(len(signStack) > 0):
                    sign = signStack.pop()
                    if(no1 == 0.5):
                        no1 = noStack.pop()
                    no2 = noStack.pop()
                    if(sign == "+"):
                        no1 = no1 + no2
                    else:
                        no1 = no1 - no2
                if(no1 == 0.5 and len(noStack) == 1):
                    no1 = noStack.pop()
                stack.append(no1)
                #print(stack)
        if(no != 0.5):
            stack.append(no)
            no = 0.5
        #print(stack)
        while(len(stack) != 0 and stack[-1] != "("):
            c = stack.pop()
            if(c == "+" or c == "-"):
                signStack.append(c)
            else:
                noStack.append(c)
        if(len(stack) > 0):
            if(stack[-1] == "("):
                stack.pop()
        no1 = 0.5
        while(len(signStack) > 0):
            sign = signStack.pop()
            if(no1 == 0.5):
                no1 = noStack.pop()
            no2 = noStack.pop()
            if(sign == "+"):
                no1 = no1 + no2
            else:
                no1 = no1 - no2
        if(no1 == 0.5 and len(noStack) == 1):
            no1 = noStack.pop()
        print(no1)
        stack.append(no1)
        return stack[-1]
