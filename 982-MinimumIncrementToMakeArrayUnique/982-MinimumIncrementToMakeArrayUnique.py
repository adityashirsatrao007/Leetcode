# Last updated: 6/4/2025, 9:21:32 PM
class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                increment = nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
                moves += increment
        return moves

# Example usage:
sol = Solution()
nums1 = [1, 2, 2]
print(sol.minIncrementForUnique(nums1))  # Output: 1

nums2 = [3, 2, 1, 2, 1, 7]
print(sol.minIncrementForUnique(nums2))  # Output: 6
