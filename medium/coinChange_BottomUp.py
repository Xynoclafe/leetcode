from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        seen = defaultdict(lambda: float("inf"))
        seen[0] = 0
        for coin in coins:
            seen[coin] = 1
        
        for i in range(amount + 1):
            amt = i
            for j in range(len(coins)):
                if coins[j] <= amt:
                    seen[amt] = min(seen[amt], seen[amt - coins[j]] + 1)
        
        return seen[amount] if seen[amount] != float("inf") else -1
