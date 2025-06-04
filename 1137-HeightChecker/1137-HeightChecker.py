# Last updated: 6/4/2025, 9:21:16 PM
class Solution:
    def heightChecker(self, heights):
        # Create the expected array by sorting the heights array
        expected = sorted(heights)
        
        # Initialize a counter for mismatches
        mismatch_count = 0
        
        # Compare each element of heights with the corresponding element in expected
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch_count += 1
        
        return mismatch_count

# Example usage
solution = Solution()

# Example 1
heights1 = [1,1,4,2,1,3]
print(solution.heightChecker(heights1))  # Output: 3

# Example 2
heights2 = [5,1,2,3,4]
print(solution.heightChecker(heights2))  # Output: 5

# Example 3
heights3 = [1,2,3,4,5]
print(solution.heightChecker(heights3))  # Output: 0
