# Last updated: 6/4/2025, 9:22:10 PM
class Solution:
    def repeatedSubstringPattern(self, s):
        n = len(s)
        
        # Iterate through possible lengths of substrings
        for len_substr in range(1, n // 2 + 1):
            # Check if s can be formed by repeating the current substring
            if n % len_substr == 0:
                substr = s[:len_substr]
                repeated_substr = substr * (n // len_substr)
                if repeated_substr == s:
                    return True
        return False

# Test cases
solution = Solution()
print(solution.repeatedSubstringPattern("abab"))          # Output: True
print(solution.repeatedSubstringPattern("aba"))           # Output: False
print(solution.repeatedSubstringPattern("abcabcabcabc"))  # Output: True
