# Last updated: 6/4/2025, 9:23:28 PM
class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        # Start from the least significant digit
        for i in range(n - 1, -1, -1):
            # Add 1 to the current digit
            digits[i] += 1
            
            # If the digit becomes 10, set it to 0 and carry over 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                # If the digit is less than 10, no carry over is needed
                return digits
        
        # If there is still a carry left, insert a new most significant digit with a value of 1
        return [1] + digits

# Test cases
solution = Solution()
print(solution.plusOne([1, 2, 3]))    # Output: [1, 2, 4]
print(solution.plusOne([4, 3, 2, 1])) # Output: [4, 3, 2, 2]
print(solution.plusOne([9]))          # Output: [1, 0]
