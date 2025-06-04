# Last updated: 6/4/2025, 9:21:38 PM
class Solution:
    def isMonotonic(self, nums):
        is_monotonic = True
        increasing = decreasing = False
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                decreasing = True
            elif nums[i] > nums[i - 1]:
                increasing = True
        
        return not increasing or not decreasing

# Test cases
solution = Solution()
print(solution.isMonotonic([1, 2, 2, 3]))  # Output: True
print(solution.isMonotonic([6, 5, 4, 4]))  # Output: True
print(solution.isMonotonic([1, 3, 2]))     # Output: False
