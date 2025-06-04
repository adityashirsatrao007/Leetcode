# Last updated: 6/4/2025, 9:19:07 PM
class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_ones = sum(nums)
        if total_ones == 0:
            return 0
        
        n = len(nums)
        # Extend the array to handle circular nature
        extended_nums = nums + nums
        
        # Initial window
        current_ones = sum(extended_nums[:total_ones])
        max_ones_in_window = current_ones
        
        # Slide the window across the extended array
        for i in range(1, n):
            current_ones += extended_nums[i + total_ones - 1] - extended_nums[i - 1]
            max_ones_in_window = max(max_ones_in_window, current_ones)
        
        # The minimum swaps required
        min_swaps = total_ones - max_ones_in_window
        return min_swaps
