class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1)
        maxLen = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                stack.pop()
                if(len(stack) > 0):
                    print(maxLen, i - stack[-1])
                    maxLen = max(maxLen, i - stack[-1])
                else:
                    stack.append(i)
        
        return maxLen
        
