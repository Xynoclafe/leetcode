from collections import defaultdict
class Solution:
    def countPrimes(self, n: int) -> int:
        
        seen = defaultdict(lambda: True)
        count = 0
        
        for i in range(2, n):
            if seen[i]:
                count += 1
                init = i * i
                while init < n:
                    seen[init] = False
                    init += i
        
        return count
        
