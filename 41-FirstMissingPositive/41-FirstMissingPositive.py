# Last updated: 6/4/2025, 9:23:41 PM
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Move each number to its correct position if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Find the first index which is not correct
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
