# Last updated: 6/4/2025, 9:20:13 PM
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        min_diff = float('inf')
        
        for i in range(4):
            min_diff = min(min_diff, nums[-(4-i)] - nums[i])
        
        return min_diff
