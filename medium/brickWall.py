from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        brickEdgeLocations = defaultdict(int)
        totLength = sum(wall[0])
        totHeight = len(wall)
        for row in wall:
            curLoc = 0
            for i in range(len(row)):
                curLoc += row[i]
                if curLoc < totLength:
                    brickEdgeLocations[curLoc] += 1
        if(len(brickEdgeLocations) == 0):
            return totHeight
        cuts = 0
        for key in brickEdgeLocations:
            cuts = max(cuts, brickEdgeLocations[key])
        return totHeight - cuts