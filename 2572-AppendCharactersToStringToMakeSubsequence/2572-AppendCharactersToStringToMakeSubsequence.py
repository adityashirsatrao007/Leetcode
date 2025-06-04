# Last updated: 6/4/2025, 9:18:32 PM
class Solution:
    def appendCharacters(self, s, t):
        s_ptr, t_ptr = 0, 0
        s_len, t_len = len(s), len(t)
        
        # Traverse both strings
        while s_ptr < s_len and t_ptr < t_len:
            if s[s_ptr] == t[t_ptr]:
                t_ptr += 1
            s_ptr += 1
        
        # The remaining characters in t to be appended
        return t_len - t_ptr

# Test cases
solution = Solution()
print(solution.appendCharacters("coaching", "coding"))  # Output: 4
print(solution.appendCharacters("abcde", "a"))         # Output: 0
print(solution.appendCharacters("z", "abcde"))         # Output: 5
