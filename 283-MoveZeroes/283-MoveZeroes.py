# Last updated: 6/4/2025, 9:22:24 PM
class Solution:
    def moveZeroes(self, nums):
        left = 0
        
        # Iterate through the array
        for right in range(len(nums)):
            # If the current element is non-zero, swap with the left pointer
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        # At the end, all non-zero elements are at the left side of the array
        # All remaining elements after left pointer are zeros
        
# Test cases
solution = Solution()
nums1 = [0, 1, 0, 3, 12]
solution.moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
solution.moveZeroes(nums2)
print(nums2)  # Output: [0]
