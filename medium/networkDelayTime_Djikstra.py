from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
                
        
        nodes = defaultdict(list)
        visited = {}
        for time in times:
            nodes[time[0]].append([time[1], time[2]])
            
        toVisit = [(0, K)]
        heapq.heapify(toVisit)
        
        while toVisit:
            time, node = heapq.heappop(toVisit)
            if node in visited:
                continue
            visited[node] = time
            for neighbor, nTime in nodes[node]:
                if neighbor not in visited:
                    heapq.heappush(toVisit, (time + nTime, neighbor))
        
        return max(visited.values()) if len(visited) == N else -1
            
        
        
        
        
        
        