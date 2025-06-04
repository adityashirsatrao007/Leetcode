# Last updated: 6/4/2025, 9:23:37 PM
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Initialize the DP table with False values
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Deal with patterns like '*' or 'a*' or '**'
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[len(s)][len(p)]

# Example usage:
solution = Solution()
print(solution.isMatch("aa", "a"))  # Output: false
print(solution.isMatch("aa", "*"))  # Output: true
print(solution.isMatch("cb", "?a"))  # Output: false
