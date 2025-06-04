# Last updated: 6/4/2025, 9:19:43 PM
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_substring(s, first, second, points):
            stack = []
            total_points = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    total_points += points
                else:
                    stack.append(char)
            return ''.join(stack), total_points
        
        if x > y:
            s, points = remove_substring(s, 'a', 'b', x)
            _, more_points = remove_substring(s, 'b', 'a', y)
        else:
            s, points = remove_substring(s, 'b', 'a', y)
            _, more_points = remove_substring(s, 'a', 'b', x)
        
        return points + more_points

# Example Usage
sol = Solution()
print(sol.maximumGain("cdbcbbaaabab", 4, 5))  # Output: 19
print(sol.maximumGain("aabbaaxybbaabb", 5, 4))  # Output: 20
