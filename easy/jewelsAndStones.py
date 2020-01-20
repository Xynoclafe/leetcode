class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewelSet = set(J)
        totalJewels = 0
        for stone in S:
            if stone in jewelSet:
                totalJewels += 1
        return totalJewels