class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        dictionary = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9}
        
        revDict = ["0", "1", "2", "3", "4", "5" ,"6", "7", "8", "9"]
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        carry = 0
        
        answer = []
        
        length = max(len(num1), len(num2))
        
        for i in range(length):
            
            int1 = 0
            int2 = 0
            
            
            if i < len(num1):
                int1 = dictionary[num1[i]]
            
            if i < len(num2):
                int2 = dictionary[num2[i]]
                
            num = int1 + int2 + carry
            
            answer.append(revDict[num % 10])
            carry = num // 10
        
        if carry != 0:
            answer.append(revDict[carry])
        
        return "".join(num for num in answer)[::-1]