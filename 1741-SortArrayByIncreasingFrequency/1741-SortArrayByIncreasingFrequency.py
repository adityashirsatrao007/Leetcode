# Last updated: 6/4/2025, 9:19:50 PM
from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Step 1: Count the frequency of each element
        freq = Counter(nums)
        
        # Step 2: Sort the elements by frequency, then by value (in decreasing order for ties)
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        
        return sorted_nums
