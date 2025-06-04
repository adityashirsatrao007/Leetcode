# Last updated: 6/4/2025, 9:20:52 PM
class Solution:
    def equalSubstring(self, s, t, maxCost):
        start = 0
        currentCost = 0
        maxLength = 0

        for end in range(len(s)):
            currentCost += abs(ord(s[end]) - ord(t[end]))

            while currentCost > maxCost:
                currentCost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            maxLength = max(maxLength, end - start + 1)

        return maxLength

# Test cases
sol = Solution()
print(sol.equalSubstring("abcd", "bcdf", 3))  # Output: 3
print(sol.equalSubstring("abcd", "cdef", 3))  # Output: 1
print(sol.equalSubstring("abcd", "acde", 0))  # Output: 1
