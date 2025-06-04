# Last updated: 6/4/2025, 9:24:31 PM
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        
        start, max_length = [0], [1]

        def expand_around_center(left, right):
            while left[0] >= 0 and right < n and s[left[0]] == s[right]:
                current_length = right - left[0] + 1
                if current_length > max_length[0]:
                    start[0] = left[0]
                    max_length[0] = current_length
                left[0] -= 1
                right += 1

        for i in range(n):
            expand_around_center([i], i)  # Odd length palindromes
            expand_around_center([i], i + 1)  # Even length palindromes

        return s[start[0]:start[0] + max_length[0]]
