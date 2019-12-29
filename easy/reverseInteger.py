class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = -x
        powr = len(str(x)) - 1
        out = 0
        while(powr >= 0):
            out += (x%10) * (10 ** powr)
            powr -= 1
            x = x//10
        if out > (2**31 - 1):
            return 0
        if flag:
            return out * (-1)
        else:
            return out
        
        
