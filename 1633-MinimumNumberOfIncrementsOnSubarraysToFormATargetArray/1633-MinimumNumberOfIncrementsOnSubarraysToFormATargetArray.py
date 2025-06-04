# Last updated: 6/4/2025, 9:20:10 PM
class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        operations = target[0]
        
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
                
        return operations

# Example usage:
solution = Solution()
print(solution.minNumberOperations([1, 2, 3, 2, 1]))  # Output: 3
print(solution.minNumberOperations([3, 1, 1, 2]))     # Output: 4
print(solution.minNumberOperations([3, 1, 5, 4, 2]))  # Output: 7
