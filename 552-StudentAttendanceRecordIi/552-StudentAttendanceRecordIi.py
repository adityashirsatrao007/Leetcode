# Last updated: 6/4/2025, 9:21:59 PM
MOD = 10**9 + 7

class Solution:
    def checkRecord(self, n):
        # Initialize the DP array with zeros
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1  # Base case: an empty sequence

        # Iterate through each length from 1 to n
        for i in range(1, n + 1):
            # Initialize the new DP array for the current length
            new_dp = [[0] * 3 for _ in range(2)]
            for A in range(2):
                for L in range(3):
                    # Add 'P'
                    new_dp[A][0] = (new_dp[A][0] + dp[A][L]) % MOD
                    # Add 'L'
                    if L > 0:
                        new_dp[A][L] = (new_dp[A][L] + dp[A][L-1]) % MOD
                    # Add 'A'
                    if A > 0:
                        new_dp[1][0] = (new_dp[1][0] + dp[0][L]) % MOD
            # Update the DP array for the next iteration
            dp = new_dp

        # Sum up all valid sequences of length n
        result = sum(sum(row) for row in dp) % MOD
        return result

# Testing the function with various test cases
if __name__ == "__main__":
    solution = Solution()

    # Example case 1
    n = 2
    print(solution.checkRecord(n))  # Expected output: 8

    # Example case 2
    n = 1
    print(solution.checkRecord(n))  # Expected output: 3

    # Additional test case
    n = 10101
    print(solution.checkRecord(n))  # Expected output: 183236316
