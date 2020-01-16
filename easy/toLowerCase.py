class Solution:
    def toLowerCase(self, s: str) -> str:
        
        newString = ""
        for i in range(len(s)):
            if ord(s[i]) in range(65, 91):
                newString += chr(ord(s[i]) + 32)
            else:
                newString += s[i]
        
        return newString