class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_time_to_buy = prices[0]
        
        ans = 0
        
        for i in range(1, len(prices)):
            if prices[i] < best_time_to_buy:
                best_time_to_buy = prices[i]
            else:
                ans = max(ans, prices[i] - best_time_to_buy)
        
        return ans