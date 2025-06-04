# Last updated: 6/4/2025, 9:18:54 PM
class Solution(object):
    def totalStrength(self, strength):
        """
        :type strength: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(strength)
        
        # Calculate prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % MOD

        # Calculate prefix of prefix sums
        prefix_of_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_of_prefix[i + 1] = (prefix_of_prefix[i] + prefix[i]) % MOD
        
        # Monotonic stack to find left and right boundaries
        left = [-1] * n
        right = [n] * n
        stack = []
        
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                right[stack.pop()] = i
            stack.append(i)
        
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                left[stack.pop()] = i
            stack.append(i)

        # Calculate total strength
        total = 0
        for i in range(n):
            l = left[i]
            r = right[i]
            left_sum = (prefix_of_prefix[i + 1] - prefix_of_prefix[l + 1]) % MOD
            right_sum = (prefix_of_prefix[r + 1] - prefix_of_prefix[i + 1]) % MOD
            total += strength[i] * (right_sum * (i - l) - left_sum * (r - i)) % MOD
            total %= MOD

        return total
