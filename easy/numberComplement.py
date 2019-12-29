class Solution:
    def toBin(self, num):
        retStr = ""
        while(num > 0):
            rem = num % 2
            num = num // 2
            retStr = str(rem) + retStr
        return retStr
    
    def findComplement(self, num: int) -> int:
        binary = self.toBin(num)
        length = len(binary)
        compString = "1"*length
        compInt = int(compString) - int(binary)
        return(int(str(compInt), 2))
