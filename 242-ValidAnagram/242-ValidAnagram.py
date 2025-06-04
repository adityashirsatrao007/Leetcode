# Last updated: 6/4/2025, 9:22:34 PM
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

# Test cases
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))         # Output: False
