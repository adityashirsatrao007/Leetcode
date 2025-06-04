# Last updated: 6/4/2025, 9:19:31 PM
class Solution:
    def arraySign(self, nums):
        sign = 1
        
        for num in nums:
            if num < 0:
                sign *= -1
            elif num == 0:
                return 0
        
        return sign

# Test cases
solution = Solution()
print(solution.arraySign([-1, -2, -3, -4, 3, 2, 1]))  # Output: 1
print(solution.arraySign([1, 5, 0, 2, -3]))          # Output: 0
print(solution.arraySign([-1, 1, -1, 1, -1]))       # Output: -1
