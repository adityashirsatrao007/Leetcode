# Last updated: 6/4/2025, 9:24:07 PM
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  # Pointer for the position of unique elements
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k
