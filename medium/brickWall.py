from collections import Counter
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        brickEdgeLocations = []
        totLength = sum(wall[0])
        totHeight = len(wall)
        for row in wall:
            curLoc = 0
            for i in range(len(row)):
                curLoc += row[i]
                if curLoc < totLength:
                    brickEdgeLocations.append(curLoc)
        print(brickEdgeLocations)
        if(len(brickEdgeLocations) == 0):
            return totHeight
        else:
            count = [count for num, count in Counter(brickEdgeLocations).most_common(1)]
            print(count)
            return (totHeight - count[0])
