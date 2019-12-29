class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        num = n
        while True:
            newNum = 0
            strNum = str(num)
            lenStrNum = len(strNum)
            for i in range(lenStrNum):
                newNum += int(strNum[i]) ** 2
            if (newNum in seen):
                return False
            elif newNum == 1:
                return True
            else:
                seen.append(newNum)
                num = newNum
                
