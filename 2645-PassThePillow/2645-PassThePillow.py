# Last updated: 6/4/2025, 9:18:23 PM
class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        # Determine the number of full cycles of passing the pillow back and forth
        cycle_length = (n - 1) * 2
        time_in_cycle = time % cycle_length

        if time_in_cycle < n:
            return time_in_cycle + 1
        else:
            return n - (time_in_cycle - (n - 1))
