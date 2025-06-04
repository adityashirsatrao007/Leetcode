# Last updated: 6/4/2025, 9:17:56 PM
class Solution:
    def scoreOfString(self, s):
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))
        return score

# Example usage:
if __name__ == "__main__":
    s1 = "hello"
    solution = Solution()
    print(solution.scoreOfString(s1))  # Output: 13

    s2 = "zaz"
    print(solution.scoreOfString(s2))  # Output: 50
