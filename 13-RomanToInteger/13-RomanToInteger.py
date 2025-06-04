# Last updated: 6/4/2025, 9:24:14 PM
class Solution:
    def romanToInt(self, s):
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        
        # Iterate through the characters of the string
        for i in range(len(s)):
            # If the current character represents a larger value than the previous character
            if i > 0 and roman_map[s[i]] > roman_map[s[i - 1]]:
                result += roman_map[s[i]] - 2 * roman_map[s[i - 1]]  # Subtract the value of the previous character
            else:
                result += roman_map[s[i]]
        
        return result

# Test cases
solution = Solution()
print(solution.romanToInt("III"))      # Output: 3
print(solution.romanToInt("LVIII"))    # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994
