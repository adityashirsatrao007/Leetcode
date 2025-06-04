# Last updated: 6/4/2025, 9:24:03 PM
class Solution:
    def removeElement(self, nums, val):
        k = 0  # Pointer for the position of non-val elements
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
