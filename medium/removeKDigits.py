class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        rem = 0
        if(k >= len(num)):
            return "0"
        while(rem < k):
            i = 0
            while i in range(len(num) - 1) and num[i] <= num[i+1]:
                i += 1
            num = num[0: i] + num[i + 1:]
            rem += 1
        flag = True
        i = 0
        while flag:
            if(num[i] == "0"):
                if(len(num) == 1):
                    flag = False
                else:
                    num = num[0: i] + num[i + 1:]
            else:
                flag = False
        return num
        
