class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if len(prices) == 0 or len(prices) == 1:
            return maxProfit
        if(len(prices) == 2):
            if(prices[0] < prices[1]):
                maxProfit = prices[1] - prices[0]
            return maxProfit
        peak = [-(10 ** 10), -1]
        through = [(10 ** 10), 10**10]
        diffs = []
        for i in range(len(prices)):
            if(i == 0):
                if(prices[i] < prices[i+1]):
                    if(through[0] > prices[i]):
                        through = [prices[i], i]
            elif(i == len(prices) - 1):
                if(prices[i] > prices[i-1]):
                    peak = [prices[i], i]
                    if(peak[1] > through[1]):
                        diffs.append(peak[0] - through[0])
            elif(prices[i] <= prices[i - 1] and prices[i] <= prices[i+1]):
                if(through[0] > prices[i]):
                    through = [prices[i], i]
            elif(prices[i] >= prices[i - 1] and prices[i] >=prices[i+1] ):
                    peak = [prices[i], i]
                    if(peak[1] > through[1]):
                        diffs.append(peak[0] - through[0])
        print(peak, through)
        if(len(diffs) == 0):
            return 0
        else:
            return max(diffs)
        
