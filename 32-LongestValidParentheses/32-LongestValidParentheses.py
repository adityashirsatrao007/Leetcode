# Last updated: 6/4/2025, 9:23:49 PM
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Initialize stack with -1 to handle edge cases
        max_len = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:  # s[i] == ')'
                stack.pop()
                if not stack:
                    stack.append(i)  # Reset with current index as new base
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
