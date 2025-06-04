# Last updated: 6/4/2025, 9:22:22 PM
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        patches = 0
        miss = 1
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        return patches

# Example usage:
solution = Solution()

nums1 = [1, 3]
n1 = 6
print(solution.minPatches(nums1, n1))  # Output: 1

nums2 = [1, 5, 10]
n2 = 20
print(solution.minPatches(nums2, n2))  # Output: 2

nums3 = [1, 2, 2]
n3 = 5
print(solution.minPatches(nums3, n3))  # Output: 0
