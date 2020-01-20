class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        length = max(len(a), len(b))
        a,b = a.zfill(length), b.zfill(length)
        
        carry = 0
        answer = []
        for i in range(length - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1
            
            answer.append("1") if carry % 2 == 1 else answer.append("0")
            
            carry //= 2
        
        if carry == 1:
            answer.append("1")
        
        return "".join(answer[::-1])