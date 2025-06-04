# Last updated: 6/4/2025, 9:24:25 PM
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # Step 2: Check for the sign
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
        
        # Step 3: Convert digits to integer
        num = 0
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1
        
        # Apply the sign
        num *= sign
        
        # Step 4: Clamp to the 32-bit signed integer range
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num

# Example usage:
solution = Solution()
print(solution.myAtoi("42"))         # Output: 42
print(solution.myAtoi("   -42"))     # Output: -42
print(solution.myAtoi("1337c0d3"))   # Output: 1337
print(solution.myAtoi("0-1"))        # Output: 0
print(solution.myAtoi("words and 987"))  # Output: 0
