# Last updated: 6/4/2025, 9:23:53 PM
class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)

# Test cases
solution = Solution()
print(solution.strStr("sadbutsad", "sad"))  # Output: 0
print(solution.strStr("leetcode", "leeto")) # Output: -1
