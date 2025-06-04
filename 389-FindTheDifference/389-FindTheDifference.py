# Last updated: 6/4/2025, 9:22:17 PM
class Solution:
    def findTheDifference(self, s, t):
        char_code = 0
        
        # XOR all characters in s
        for char in s:
            char_code ^= ord(char)
        
        # XOR all characters in t
        for char in t:
            char_code ^= ord(char)
        
        # The result will be the ASCII of the extra character
        return chr(char_code)

# Test cases
solution = Solution()
print(solution.findTheDifference("abcd", "abcde"))  # Output: "e"
print(solution.findTheDifference("", "y"))          # Output: "y"
