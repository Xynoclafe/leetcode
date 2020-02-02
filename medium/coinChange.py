from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        seen = defaultdict(lambda: -1)
        seen[0] = 0
        
        for coin in coins:
            seen[coin] = 1
        
        def changeCoin(amount):
            
            if amount < 0:
                return float("inf")
            
            if seen[amount] > -1:
                return seen[amount]
            
            minm = float("inf")
            
            for coin in coins:
                minm = min(minm, changeCoin(amount - coin) + 1)
                
            seen[amount] = minm
            
            return seen[amount]
        
        minm = changeCoin(amount)
        
        return minm if minm != float("inf") else -1
