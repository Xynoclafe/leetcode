class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            minCost.append(min(minCost[i - 1], minCost[i - 2]) + cost[i])
            
        return min(minCost[len(cost) - 1], minCost[len(cost) - 2])