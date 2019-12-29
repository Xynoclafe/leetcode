class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        revNum = 0
        if(x < 0):
            return False
        length = len(str(x))
        power = 10 ** (length - 1)
        while(num != 0):
            revNum += (num%10) * power
            power = power/10
            num = num // 10
        newX = int(revNum)
        if(newX == x):
            return True
        else:
            return False
