# Last updated: 6/4/2025, 9:19:55 PM
class Solution:
    def specialArray(self, nums):
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] >= n - i:
                if i == 0 or nums[i-1] < n - i:
                    return n - i
        return -1

# Test case
solution = Solution()
print(solution.specialArray([3, 6, 7, 7, 0]))  # Output: -1
