from collections import defaultdict
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        seenMin = defaultdict(int)
        
        def getDist(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
        
        def findPairs(workerIndex, availableBikes):
            if workerIndex == len(workers):
                return 0
            
            if (workerIndex, tuple(availableBikes)) in seenMin:
                return seenMin[(workerIndex, tuple(availableBikes))]
            
            worker = workers[workerIndex]
            minm = (10 ** 10)
            
            for i in range(len(availableBikes)):
                if availableBikes[i]:
                    minm = min(minm, getDist(worker, bikes[i]) + findPairs(workerIndex + 1, availableBikes[:i] + [False] + availableBikes[i+1:]))
                    
            seenMin[(workerIndex, tuple(availableBikes))] = minm
            return minm
        
        return findPairs(0, [True] * len(bikes))
