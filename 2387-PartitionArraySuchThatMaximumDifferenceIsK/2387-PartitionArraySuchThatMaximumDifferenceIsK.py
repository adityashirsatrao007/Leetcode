# Last updated: 6/4/2025, 9:18:51 PM
class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 1
        min_val = nums[0]
        
        for num in nums:
            if num - min_val > k:
                count += 1
                min_val = num
        
        return count
