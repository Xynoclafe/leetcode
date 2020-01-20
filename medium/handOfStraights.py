import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        heapq.heapify(hand)
        curSet = []
        unused = []
        while hand:
            curSet.append(heapq.heappop(hand))
            while len(curSet) < W and hand:
                element = heapq.heappop(hand)
                if element == curSet[-1] + 1:
                    curSet.append(element)
                else:
                    unused.append(element)
            while unused:
                heapq.heappush(hand, unused.pop())
            if len(curSet) < W:
                return False
            else:
                curSet = []
        return True