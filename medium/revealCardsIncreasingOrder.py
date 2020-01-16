from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        numCards = len(deck)
        indices = deque([i for i in range(numCards)])
        returnDeck = [None] * numCards
        
        for card in sorted(deck):
            index = indices.popleft()
            returnDeck[index] = card
            if len(indices) > 0:
                indices.append(indices.popleft())
        return returnDeck