from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        position = defaultdict(set)
        guessPosition = defaultdict(set)
        A = 0
        B = 0
        
        for i in range(len(secret)):
            num = secret[i]
            position[num].add(i)
        
        for i in range(len(guess)):
            num = guess[i]
            guessPosition[num].add(i)
            
        for key in guessPosition:
            bulls = guessPosition[key].intersection(position[key])
            cow1 = guessPosition[key] - bulls
            cow2 = position[key] - bulls
            
            
            
            if len(bulls) > 0:
                A += len(bulls)
            if len(position[key]) > 0:
                B += min(len(cow2), len(cow1))
            
        return str(A) + "A" + str(B) + "B"