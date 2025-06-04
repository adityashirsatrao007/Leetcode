# Last updated: 6/4/2025, 9:17:43 PM
class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        
        def backtrack(current, idx):
            if len(current) == n:
                results.append("".join(current))
                return
            
            # Try to append '0' if it does not violate the condition
            if idx == 0 or current[idx - 1] != '0':
                current.append('0')
                backtrack(current, idx + 1)
                current.pop()
            
            # Always append '1' since it does not violate the condition
            current.append('1')
            backtrack(current, idx + 1)
            current.pop()
        
        backtrack([], 0)
        return results

# Example usage:
solution = Solution()
print(solution.validStrings(3))  # Output: ["010", "011", "101", "110", "111"]
print(solution.validStrings(1))  # Output: ["0", "1"]
