# Last updated: 6/4/2025, 9:20:25 PM
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        count = 0
        
        for j in range(n):
            left_smaller = left_larger = right_smaller = right_larger = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                if rating[i] > rating[j]:
                    left_larger += 1
            
            for k in range(j+1, n):
                if rating[k] > rating[j]:
                    right_larger += 1
                if rating[k] < rating[j]:
                    right_smaller += 1
            
            count += left_smaller * right_larger + left_larger * right_smaller
        
        return count
