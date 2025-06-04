# Last updated: 6/4/2025, 9:19:28 PM
class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        winner = 0
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1
