# Last updated: 6/4/2025, 9:24:23 PM
class Solution:
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        # Numbers ending in 0 (but not 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # If the number of digits is odd, we need to remove the middle digit from reversed_half
        return x == reversed_half or x == reversed_half // 10

# Example usage
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121)) # Output: False
print(solution.isPalindrome(10))   # Output: False
