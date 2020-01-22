from collections import defaultdict
from collections import deque
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        indices = defaultdict(lambda: deque([]))
        
        for i in range(len(source)):
            indices[source[i]].append(i)
            
        count = 1
            
        curChar = -1
        
        for char in target:
            if len(indices[char]) == 0:
                return -1
            newIndex = (bisect.bisect(indices[char], curChar))
            if newIndex == len(indices[char]):
                count += 1
                curChar = indices[char][0]
            else:
                curChar = indices[char][newIndex]
        
        return count
