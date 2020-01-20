from collections import deque
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        taken = set({})
        returnList = [-1] * len(workers)
        distList = deque([])
        heap = []
        for i in range(len(workers)):
            worker = workers[i]
            distances = []
            for j in range(len(bikes)):
                bike = bikes[j]
                dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances.append((dist, i, j))
            heapq.heapify(distances)
            distList.append(distances)
        
        heapq.heapify(heap)
        for i in range(len(workers)):
            heapq.heappush(heap, heapq.heappop(distList[i]))
        
        while heap:
            pair = heapq.heappop(heap)
            if pair[2] not in taken:
                taken.add(pair[2])
                returnList[pair[1]] = pair[2]
            else:
                heapq.heappush(heap, heapq.heappop(distList[pair[1]]))
        
        return returnList
                
        
