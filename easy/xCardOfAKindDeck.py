from collections import defaultdict
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        counts = defaultdict(int)
        for card in deck:
            counts[card] += 1
        
        minCount = 0
        for card in counts:
            minCount = gcd(minCount, counts[card])
        
        if minCount < 2:
            return False
        
        for card in counts:
            if counts[card] % minCount != 0:
                return False
        
        return True
            