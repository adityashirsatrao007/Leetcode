# Last updated: 6/4/2025, 9:23:29 PM
import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = list(range(1, n + 1))
        k -= 1  # Convert k to 0-based index
        factorial = math.factorial(n)
        result = []
        
        for i in range(n, 0, -1):
            factorial //= i
            index = k // factorial
            result.append(str(numbers.pop(index)))
            k %= factorial
        
        return ''.join(result)

# Example usage:
solution = Solution()
print(solution.getPermutation(3, 3))  # Output: "213"
print(solution.getPermutation(4, 9))  # Output: "2314"
print(solution.getPermutation(3, 1))  # Output: "123"
