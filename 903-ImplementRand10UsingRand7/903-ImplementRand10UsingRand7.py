# Last updated: 6/4/2025, 9:21:41 PM
import random

# Mock rand7() for testing
def rand7():
    return random.randint(1, 7)

class Solution:
    def rand10(self):
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return 1 + (num - 1) % 10

# Example usage
sol = Solution()
n = 2  # Number of times to call rand10()
result = [sol.rand10() for _ in range(n)]
print(result)  # Output the result
