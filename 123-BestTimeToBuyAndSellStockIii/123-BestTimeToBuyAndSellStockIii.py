# Last updated: 6/4/2025, 9:23:12 PM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        n = len(prices)
        max_profit = 0
        max_profit_from_left = [0] * n
        max_profit_from_right = [0] * n
        
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            max_profit_from_left[i] = max(max_profit_from_left[i-1], prices[i] - min_price)
        
        max_price = prices[-1]
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i])
            max_profit_from_right[i] = max(max_profit_from_right[i+1], max_price - prices[i])
        
        for i in range(n):
            max_profit = max(max_profit, max_profit_from_left[i] + max_profit_from_right[i])
        
        return max_profit
