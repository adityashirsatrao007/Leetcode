# Last updated: 6/4/2025, 9:24:26 PM
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Handle sign
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        
        # Convert to string, reverse, and convert back to integer
        reversed_x_str = str(x)[::-1]
        reversed_x = int(reversed_x_str) * sign
        
        # Check for overflow
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        return reversed_x

# Example usage:
solution = Solution()
print(solution.reverse(123))    # Output: 321
print(solution.reverse(-123))   # Output: -321
print(solution.reverse(120))    # Output: 21
