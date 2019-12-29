class Solution:
    def intToRoman(self, num: int) -> str:
        newList = [1000, 500, 100, 50, 10, 5, 1]
        remList = []
        outStr = ""
        for i in newList:
            rem = num // i
            num = num % i
            remList.append(rem)
        outStr = remList[0] * "M" + remList[1] * "D" + remList[2] * "C" + remList[3] * "L" + remList[4] * "X" + remList[5] * "V" + remList[6] * "I"
        outStr = outStr.replace("DCCCC", "CM")
        outStr = outStr.replace("CCCC", "CD")
        outStr = outStr.replace("LXXXX", "XC")
        outStr = outStr.replace("XXXX", "XL")
        outStr = outStr.replace("VIIII", "IX")
        outStr = outStr.replace("IIII", "IV")
        return outStr
