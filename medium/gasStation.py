class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        
        if n == 0 or sum(cost) > sum(gas):
            return -1
        
        start = None
        
        for i in range(n):
            if cost[i] <= gas[i]:
                start = i
                break
        
        curPoint = start
        curGas = gas[start]

        while i < n:
            if curGas - cost[curPoint] >= 0:
                curGas -= cost[curPoint]
                curPoint = (curPoint + 1) % n
                curGas += gas[curPoint]
                i += 1
            else:
                start = (curPoint + 1) % n
                curPoint = start
                curGas = gas[start]
                i = 0
        
        return start
