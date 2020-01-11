from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        def dfs(node, count):
            if node in visited and counts[node] <= count:
                return
            else:
                counts[node] = count
                visited.add(node)
            for element in sorted(nodes[node], key = lambda x: x[1]):
                dfs(element[0], count + element[1])
            return
                
        
        nodes = defaultdict(list)
        counts = defaultdict(lambda: 10 ** 10)
        visited = set({})
        for time in times:
            nodes[time[0]].append([time[1], time[2]])
            
        dfs(K, 0)
        maxm = 0
        for i in range(N):
            maxm = max(maxm, counts[i + 1])
        
        return maxm if maxm != (10 ** 10) else -1
        
        
        
        
        