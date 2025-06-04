# Last updated: 6/4/2025, 9:22:13 PM
from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        char_count = Counter(s)
        length = 0
        odd_found = False
        
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        
        # If there was at least one character with an odd count, add one to the length for the center character
        if odd_found:
            length += 1
        
        return length

# Test cases
solution = Solution()
print(solution.longestPalindrome("abccccdd"))  # Output: 7
print(solution.longestPalindrome("a"))         # Output: 1
print(solution.longestPalindrome("Aa"))        # Output: 1
print(solution.longestPalindrome("abc"))       # Output: 1
print(solution.longestPalindrome("abccccba"))  # Output: 7
