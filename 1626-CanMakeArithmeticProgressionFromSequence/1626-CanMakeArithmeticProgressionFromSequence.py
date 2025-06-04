# Last updated: 6/4/2025, 9:20:11 PM
class Solution:
    def canMakeArithmeticProgression(self, arr):
        # Sort the array in ascending order
        arr.sort()
        
        # Calculate the common difference between consecutive elements
        common_diff = arr[1] - arr[0]
        
        # Check if all differences between consecutive elements are equal
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != common_diff:
                return False
        
        return True

# Test cases
solution = Solution()
print(solution.canMakeArithmeticProgression([3, 5, 1]))  # Output: True
print(solution.canMakeArithmeticProgression([1, 2, 4]))  # Output: False
