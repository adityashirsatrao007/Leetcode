# Last updated: 6/4/2025, 9:22:50 PM
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k == 0:
            return 0
        
        n = len(prices)
        if k >= n // 2:
            # If k is large enough to cover all possible transactions, use a greedy approach
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    max_profit += prices[i] - prices[i-1]
            return max_profit
        
        # Use dynamic programming approach for arbitrary k
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)
        
        for price in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j-1] - price)
                sell[j] = max(sell[j], buy[j] + price)
        
        return sell[k]
