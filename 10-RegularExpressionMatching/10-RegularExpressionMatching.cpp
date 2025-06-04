// Last updated: 6/4/2025, 9:24:21 PM
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length();
        int n = p.length();
        
        // Initialize DP array
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Empty string and empty pattern match
        dp[0][0] = true;
        
        // Handling patterns like "a*", ".*", "c*a*b*", etc.
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }
        
        // DP traversal
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == p[j - 1] || p[j - 1] == '.') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'));
                }
            }
        }
        
        return dp[m][n];
    }
};
