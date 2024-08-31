# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        min = prices[0]
        diff = 0

        for i in range(1, len(prices)):
            if prices[i] - min > diff:
                diff = prices[i] - min
            
            elif prices[i] < min:
                min = prices[i]

        return diff