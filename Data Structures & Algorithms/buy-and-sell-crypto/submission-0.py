class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0
        for i in range(len(prices)):
            res = max(res, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        
        return res

        
        
