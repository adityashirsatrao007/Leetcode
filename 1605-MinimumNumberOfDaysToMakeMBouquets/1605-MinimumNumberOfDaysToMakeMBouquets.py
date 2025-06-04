# Last updated: 6/4/2025, 9:20:16 PM
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def canMakeBouquets(days):
            bouquets = 0
            flowers = 0
            
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            
            return bouquets >= m

        n = len(bloomDay)
        if n < m * k:
            return -1
        
        low, high = min(bloomDay), max(bloomDay)
        
        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(mid):
                high = mid
            else:
                low = mid + 1
        
        return low if canMakeBouquets(low) else -1
