# Last updated: 6/4/2025, 9:20:59 PM
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if char == ')':
                # Start popping until we find the opening parenthesis '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the opening parenthesis '('
                stack.pop()
                # Reverse the characters and push them back to stack
                stack.extend(temp)
            else:
                stack.append(char)
        
        # Join the characters in stack to form the final result
        return ''.join(stack)

# Example usage:
# solution = Solution()
# print(solution.reverseParentheses("(abcd)"))          # Output: "dcba"
# print(solution.reverseParentheses("(u(love)i)"))      # Output: "iloveu"
# print(solution.reverseParentheses("(ed(et(oc))el)"))  # Output: "leetcode"
