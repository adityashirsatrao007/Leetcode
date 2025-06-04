# Last updated: 6/4/2025, 9:22:20 PM
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

# Test cases
s1 = ["h","e","l","l","o"]
print(Solution().reverseString(s1))  # Output: ["o", "l", "l", "e", "h"]

s2 = ["H","a","n","n","a","h"]
print(Solution().reverseString(s2))  # Output: ["h", "a", "n", "n", "a", "H"]
