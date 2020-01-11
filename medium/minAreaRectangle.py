from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        xIndices = defaultdict(list)
        for point in points:
            xIndices[point[0]].append(point[1])
        
        ans = float("inf")
        lastx = {}
        
        for x in sorted(xIndices):
            column = xIndices[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float("inf") else 0
                