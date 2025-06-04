# Last updated: 6/4/2025, 9:19:20 PM
class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        # Sort both the seats and students arrays
        seats.sort()
        students.sort()
        
        # Calculate the sum of absolute differences between paired elements
        total_moves = sum(abs(seats[i] - students[i]) for i in range(len(seats)))
        
        return total_moves
