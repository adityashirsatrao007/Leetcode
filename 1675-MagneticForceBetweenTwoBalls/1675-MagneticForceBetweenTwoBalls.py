# Last updated: 6/4/2025, 9:20:01 PM
class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        # Helper function to determine if we can place m balls with minimum distance d
        def canPlaceBalls(d):
            count = 1  # First ball is always placed
            last_position = position[0]  # Place the first ball at the first position
            
            for i in range(1, len(position)):
                if position[i] - last_position >= d:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        position.sort()
        
        left, right = 1, position[-1] - position[0]
        answer = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return answer
