class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        memTable = [[False for _ in range(length)] for _ in range(length)]
        largest = [0, [0, 0]]
        if(length == 0):
            return ""
        for i in range(length):
            memTable[i][i] = True
            if largest[0] < 1:
                largest[0] = 1
                largest[1] = [i, i]
            if i < length - 1 and s[i] == s[i + 1]:
                if largest[0] < 2:
                    largest[0] = 2
                    largest[1] = [i, i+1]
                memTable[i][i+1] = True
                
        for j in range(length):
            for i in range(j - 1):
                if s[i] == s[j] and memTable[i+1][j-1]:
                    memTable[i][j] = True
                    if largest[0] < j - i + 1:
                        largest[0] = (j - i + 1)
                        largest[1] = [i, j]

        return s[largest[1][0]:largest[1][1] + 1]
        
